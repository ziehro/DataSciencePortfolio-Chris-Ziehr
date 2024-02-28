# EMFDataInsights: Understanding Plant Communications through EMF

## Project Overview

This project explores the electromagnetic field (EMF) responses from mycelium in a plant pot using a Hall effect sensor. The goal is to investigate if plants communicate or respond to environmental changes through detectable EMF variations. We map these EMF readings to a color scale, visually represented on a light strip, creating a dynamic interaction reflecting the plant's condition. This repository contains the data collection, analysis, and visualization scripts, alongside the AI models developed to identify patterns within the EMF data.

## Technical Description

The setup involves a Hall effect sensor connected through an Analog-to-Digital Converter (ADC) to a Raspberry Pi. Sensor readings, representing the EMF responses, are mapped to specific colors on a light strip, creating a visual feedback mechanism from the plant. The data is transmitted in real-time to Firebase, enabling live data analysis and visualization on a dedicated website.

### Components

- Hall effect sensor
- ADC (Analog-to-Digital Converter)
- Raspberry Pi
- LED light strip
- Firebase for real-time data storage

## Installation

Instructions for setting up the hardware and software environment are detailed in the [Installation Guide](/installation.md). This includes setting up the Raspberry Pi, connecting the sensor and light strip, and configuring Firebase.

## Usage

Detailed instructions on how to run the scripts, collect data, and perform analysis are provided in the [Usage Guide](/usage.md). This includes:

- `sensor_readings.py`: Script to collect data from the Hall effect sensor.
- `data_analysis.ipynb`: Jupyter notebook for initial data analysis, including FFT and gain control.
- `visualization.html`: HTML code for the data visualization website.

## Data Visualization

Screenshots and a link to the live data visualization website are included. The website features real-time graphs of the EMF data collected from the plant, offering insights into its response patterns.

## Analysis and Results

The `analysis` directory contains Python scripts and Jupyter notebooks detailing the data analysis process, including Fast Fourier Transform (FFT) applications, gain adjustments, and frequency analysis. We discuss the identified patterns, their potential meanings, and the implications for understanding plant communications.

## AI and Pattern Detection

We employ machine learning algorithms to detect patterns within the EMF data. This section explains the chosen algorithms, the rationale behind them, and the insights gained from the AI analysis. Details on how to run the AI models and interpret their outputs are provided.

## Replication and Contribution

Instructions for replicating the experiment and contributing to the project are outlined here. This includes a list of required materials, software setup steps, and how to contribute data or code improvements.

## Reflections and Future Work

A discussion of the project's outcomes, challenges faced, and how they were addressed. This section also outlines future research directions and potential improvements to the project.

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to XXX for their contributions and support throughout this project.


