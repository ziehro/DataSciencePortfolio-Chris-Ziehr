

import firebase_admin
from firebase_admin import credentials, db
from GraphDataProcessor import GraphDataProcessor  # Ensure this matches your module's name
import time
from datetime import datetime
from sensor_led_control_mixed import SensorColorMapper, update_leds, read_sensor
import socket
import threading
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
from rpi_ws281x import PixelStrip, Color

# Configuration for LED strip.
LED_PIN = 10
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 2  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
NUM_LEDS = 29

# Initialize the LED strip.
strip = PixelStrip(NUM_LEDS, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Initialize Firebase configuration and app.
firebase_config = {
  "apiKey": "AIzaSyBALu3RCT6r4wN9COgIwofLy7RCPRXaN6E",
  "authDomain": "myceliumemf.firebaseapp.com",
  "databaseURL": "https://myceliumemf-default-rtdb.firebaseio.com",
  "projectId": "myceliumemf",
  "storageBucket": "myceliumemf.appspot.com",
  "messagingSenderId": "1011466135526",
  "appId": "1:1011466135526:web:5ae70c9aacdd47a9395827",
  "measurementId": "G-32X7EGZ54E"
}

cred = credentials.Certificate("/home/ziehro/plantlight/firebase-sdk.json")
firebase_admin.initialize_app(cred, firebase_config)

graph_processor = GraphDataProcessor()
sensor_color_mapper = SensorColorMapper()

# Setup ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1
ads.data_rate = 16  # Adjust as needed for your application
incomingRate = 10
print ("Ready")
# Setup socket
HOST = ''  # Listen on all interfaces
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

print(f'Connected by {addr}')

channel = AnalogIn(ads, ADS.P0)

def check_for_commands():
    global ads, incomingRate
    while True:
        try:
            conn.settimeout(1)  # Short timeout for non-blocking receive
            data = conn.recv(1024).decode('utf-8')
            if data.startswith('SET_GAIN:'):
                _, gain_value = data.split(':')
                ads.gain = int(gain_value)
                print(f"Gain set to {gain_value}")
            elif data.startswith('SET_SAMPLING_RATE:'):
                _, rate_value = data.split(':')
                incomingRate = int(rate_value)
                print(f"Sampling rate set to {rate_value} SPS")
        except socket.timeout:
            continue  # Skip iteration and continue listening for commands
        except Exception as e:
            print(f"Error receiving command: {e}")
        finally:
            conn.settimeout(None)  # Reset to blocking mode
        time.sleep(10)  # Delay before next command check

# Start the command checking in a separate thread
threading.Thread(target=check_for_commands, daemon=True).start()


def main():
    last_update_time = time.time()

    try:
        while True:
            sensor_reading = read_sensor()
            message = f'{sensor_reading}\n'.encode()
            conn.sendall(message)  # Send sensor data over the socket
            sensor_color_mapper.add_sensor_reading(sensor_reading)
            packed_color = sensor_color_mapper.map_value_to_color()  # Assumes returning RGB packed as integer
        
        # Unpack RGB values
            update_leds(packed_color)

            # Add sensor data for processing
            # graph_processor.add_data(sensor_reading * 1000)  # Assuming sensor_reading needs scaling

            current_time = time.time()

            if current_time - last_update_time >= 60:
                rolling_averages = graph_processor.calculate_rolling_average(window_size=20)
                latest_average = rolling_averages[-1] if rolling_averages else None

                candlestick_data = graph_processor.prepare_candlestick_data(interval=500)
                latest_candle = candlestick_data[-1] if candlestick_data else None


            # Push the latest rolling average to Firebase
                if latest_average is not None:
                     db.reference('rolling_averages_moist').push({
                      'timestamp': datetime.now().isoformat(),
                     'average': latest_average
                     })

            # Push the latest candlestick data to Firebase
                if latest_candle is not None:
              # Directly use latest_candle if it's already a dictionary
                  latest_candle_py = {k: graph_processor.convert_to_python(v) for k, v in latest_candle.items()}

                  db.reference('candlestick_data').push({
                 
                    'data': latest_candle_py
                  })

            last_update_time = current_time

            time.sleep(1/incomingRate)  # Short sleep to reduce CPU usage

    except KeyboardInterrupt:
        print("\nProgram terminated.")
    finally:
        conn.close()  # Close the socket connection
        s.close()  # Close the server socket

if __name__ == "__main__":
    main()
