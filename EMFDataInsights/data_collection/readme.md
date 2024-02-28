## Data Collection and Visualization

This section of the project outlines the procedures for data collection and visualization. Data is collected through a Raspberry Pi equipped with a Hall effect sensor. The sensor values are transmitted via WiFi to a local machine using the Python script `[emfSendSignal.py](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/scripts/emfSendSignal.py)`. Additionally, this script controls an LED light strip to visualize the sensor readings in real time.

The data is then processed by the local machine using `[emfReceiveSignal.py](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/scripts/emfReceiveSignal.py)`. This script reads the incoming signals and plots them in real-time using a Matplotlib graph. The graph includes radio buttons that allow users to adjust settings such as the gain and frequency of the PGA (Programmable Gain Amplifier) connected to the sensor. It also facilitates event recording; users can specify the duration, title, and description of an event, and the software will record the data for the specified time. The event description, along with the data, is saved in a JSON file, and a plot of the event and its timeframe is also saved to disk.

Additionally, every 10 minutes, the Raspberry Pi uploads a data dump to Firestore, enabling real-time visualization on the project website.

### Key Features:

- **Real-time Data Visualization**: Visualize sensor readings in real-time on an LED light strip and through Matplotlib graphs.
  ![Real-time Data Visualization](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/data_collection/images/realtime.png)
- **Event Recording**: Specify event duration, title, and description for targeted data collection and analysis.
  ![Event Recording](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/images/data_collection/event_recording.png)
- **Cloud Integration**: Automatic data uploads to Firestore for web visualization.
  ![Cloud Integration](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/images/website_image.png)

### Resources and Links:

- **Code**:
  - [emfSendSignal.py](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/scripts/emfSendSignal.py)
  - [emfReceiveSignal.py](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/scripts/emfReceiveSignal.py)
- **Live Data Visualization**: [driftwest.xyz](http://driftwest.xyz)
- **Graph Images**: See [images folder](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/images) for plots and event visualizations.

### Website Features:

- **Event Marking**: Mark and annotate specific events directly through the website interface.
  ![Event Marking](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/images/event_marking.png)
- **Environmental Data Display**: Options to display temperature and humidity data alongside EMF sensor readings for comprehensive environmental analysis.
  ![Environmental Data Display](https://github.com/<ziehro>/DataSciencePortfolio-Chris-Ziehr/EMFDataInsights/tree/master/images/environmental_display.png)

