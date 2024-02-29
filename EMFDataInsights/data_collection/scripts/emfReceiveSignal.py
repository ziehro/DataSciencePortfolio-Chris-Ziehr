import socket
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from FFTAnalyzer import FFTAnalyzer
from gui_components_mixed import setup_gui_components, add_autoscale_button
from event_module import get_user_input, save_event_data
import threading
import queue
import time

collecting_data = False
event_readings = []
time_events = []  # To store the timestamps of 'T' key presses
event_title = "Title"
event_description = "Description"
event_seconds = "20"

# Global flag to control pausing and queue for FFT analysis
is_paused = False
fft_queue = queue.Queue()

# TCP/IP Setup for Client
HOST = '192.168.43.214'  # IP address of the Raspberry Pi
PORT = 65432  # Port to connect to

# Connect to the Raspberry Pi server
global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(0)  # Set socket to non-blocking mode

# Initialize plot
fig, ax = plt.subplots()
# plt.subplots_adjust(left=0.15, bottom=0.15)
ln, = ax.plot([], [], 'r-')  # Initialize line object
ax.set_xlim(0, 99)
ax.set_ylim(0.5, 0.7)
x_data, y_data = [0], [0.61]  # Start with an initial data point


new_readings_count = 0
autoscale_enabled = False  # Global flag for autoscale

# FFT Analyzer
fft_analyzer = FFTAnalyzer(batch_size=100000)

def onclick(event):
    global is_paused
    # Check if the click was on the canvas and not on a widget
    if event.inaxes == ax:
        is_paused = not is_paused



def toggle_autoscale():
    global autoscale_enabled
    autoscale_enabled = not autoscale_enabled
    print("Autoscale is now", "enabled" if autoscale_enabled else "disabled")
    if not autoscale_enabled:
        # Set manual limits if autoscale is turned off
        ax.set_ylim([0.55, 0.65])  
    autoscale_button.color = 'green' if autoscale_enabled else '0.85'  # '0.85' is a default gray
    autoscale_button.hovercolor = '0.95'  # Lighter gray for hover if you want to change that as well
    fig.canvas.draw_idle()

autoscale_button = add_autoscale_button(ax, fig, toggle_autoscale)      

class PlotSettings:
    def __init__(self):
        self.autoscale_enabled = True
        self.x_min = 0
        self.x_max = 100
        self.y_min = 0.55
        self.y_max = 0.65

# Initialize settings
plot_settings = PlotSettings()

def on_key_press(event):
    global collecting_data, start_time, time_events, event_title, event_description, event_seconds
    current_time = time.time()

    if event.key == 'e':  # Assuming 't' is the key for the touch event
        print("Touch event recorded at index:", len(y_data))
        fft_analyzer.mark_event(len(y_data))  # If you're marking events for FFT analysis
        
        # Add a vertical line to the plot at the index of the latest data point
        if len(y_data) > 0:  # Ensure there is data
            current_index = len(y_data) - 1  # Index of the latest data point
            ax.axvline(x=current_index, color='g', linestyle='--')  # Add a green vertical line
            
            # Optionally, you might want to add a label or text to the line
            # ax.text(current_index, ax.get_ylim()[1], 'Touch Event', rotation=90, verticalalignment='top')
            
            fig.canvas.draw_idle()  # Redraw the plot to show the new line

    if event.key == 't' and collecting_data:
        elapsed_time = current_time - start_time
        if 0 <= elapsed_time <= 120:
          time_events.append(elapsed_time)  # Store the elapsed time of the event
          print(f"Time event recorded at {elapsed_time} seconds.")

    elif event.key == '+':
        if not collecting_data:  # To prevent overlapping with ongoing data collection
            event_title, event_description, event_seconds = get_user_input()
            if event_title and event_description and event_seconds:
                start_time = time.time()
                collecting_data = True
                # Clear previous readings and time events
                global event_readings
                event_readings = []
                time_events = []
                print("Started data capture for ")
    

    

# Function to handle batch data analysis
def handle_fft_analysis():
    while True:
        batch_data = fft_queue.get()  # Wait until a batch is available
        fft_analyzer.analyze_and_plot(batch_data, event_title)
        fft_queue.task_done()



# Update function for the plot
def update(frame):
    global x_data, y_data, new_readings_count, data_ready, event_readings, collecting_data, fft_analyzer, event_title
    if not is_paused:
        try:
            data_ready = False
            while True:
                data = s.recv(1024).decode('utf-8').strip()
                if not data:
                    break  # If no data, exit loop
                new_y_values = [float(value) for value in data.split('\n') if value]
                y_data.extend(new_y_values)
                new_readings_count += len(new_y_values)
                
                # Only keep the most recent data for plotting to maintain performance
                if len(y_data) > 2000:  # Example: Keep twice the batch size for smooth plotting
                    y_data = y_data[-2000:]
                    x_data = list(range(len(y_data)))

                data_ready = True

                if collecting_data:
                    current_time = time.time()
                    elapsed_time = current_time - start_time  # Time since data collection started
                    if elapsed_time <= int(event_seconds): 
                        for value in new_y_values:  # Assuming new_y_values is a list of new data points
            # Append a tuple of (elapsed time, value) for each new value
                              event_readings.append((elapsed_time, value))
                    else:
                # Stop collecting data after 2 minutes
                        collecting_data = False
                        save_event_data(event_title, event_description, event_readings, time_events)
                        # Extract just the sensor values from event_readings
                        sensor_values = [value for _, value in event_readings]
                        fft_analyzer.analyze_and_plot(sensor_values, event_title)

                
                # Check if we have enough new readings for a batch analysis
                if new_readings_count >= fft_analyzer.batch_size:
                    # Send the most recent batch_size readings for FFT analysis
                    batch_data = y_data[-fft_analyzer.batch_size:]
                    fft_queue.put(batch_data)
                    new_readings_count = 0  # Reset new readings count after sending a batch

        except BlockingIOError:
            pass  # No more data available to read
        

    if data_ready:
        if len(y_data) > 100:
            plot_y_data = y_data[-100:]  # Get the last 100 points
            plot_x_data = list(range(len(y_data) - 100, len(y_data)))  # Adjust x_data to match
        else:
            plot_y_data = y_data
            plot_x_data = list(range(len(y_data)))

        ln.set_data(plot_x_data, plot_y_data)
        if autoscale_enabled:
            ax.relim()  # Recompute the data limits based on the updated data
            ax.autoscale(enable=True, axis='y')
            ax.autoscale_view()  # Autoscale the view limits

            fig.canvas.draw_idle()  # Redraw the figure to update the axes and data
            ax.set_xlim(max(0, len(y_data) - 100), len(y_data) - 1)  # Set x-axis limits
        else:
            ax.set_ylim(plot_settings.y_min, plot_settings.y_max)
            fig.canvas.draw_idle()  # Redraw the figure to update the axes and data
            ax.set_xlim(max(0, len(y_data) - 100), len(y_data) - 1)  # Set x-axis limits


fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Assuming s is your socket object connected to the Raspberry Pi


# Start the thread for handling FFT analysis
fft_thread = threading.Thread(target=handle_fft_analysis, daemon=True)
fft_thread.start()

# FuncAnimation for real-time plotting
ani = FuncAnimation(fig, update, blit=False, interval=100)
setup_gui_components(ax, s, fig, plot_settings)

plt.show()

s.close()


