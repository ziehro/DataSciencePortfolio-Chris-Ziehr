# Data Analysis Tools

This directory contains tools and scripts for real-time data analysis and event recording for the EMFDataInsights project.

## Overview

The primary tool in this folder is a Python script utilizing Matplotlib to create a dynamic graph that plots EMF data in real time, similar to an oscilloscope display. This tool allows for live data monitoring and analysis of trends based on the most recent 100 readings.

## Features

- **Real-Time Data Plotting**: Continuously updates and scrolls through the latest 100 EMF readings.
- **Event Recording**: By pressing the '+' key, users can input event details (duration, title, description) and record specific data segments into a JSON file.
- **Timestamp Marking**: Press 't' during event recording to insert a timestamp marker into the graph, highlighting specific points of interest.
- **Graph Export**: Automatically generates and saves a PNG image of the plotted data, with vertical indicator lines for each timestamp.

## Usage

1. Navigate to the script directory: `cd path_to_your_project/EMFDataInsights/data_analysis`
2. Run the script: `python matplotlib_realtime.py`
3. Follow the on-screen instructions to record events and insert timestamps.

## Resources

- **Scripts**:
  - Real-time plotting: [matplotlib_realtime.py](../data_collection/scripts/emfReceiveSignal.py)
- **Images**:
  - Example plots: [View here](./images/)

Please ensure you have the necessary Python dependencies installed before running the scripts.

## Contributing

Feedback and contributions to this analysis tool are welcome. Please submit issues and pull requests to the main repository or contact the project maintainers directly.


