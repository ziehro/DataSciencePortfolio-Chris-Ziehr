# EMF Data Insights: Understanding Plant Communications through EMF

## Project Overview

EMF Data Insights is a pioneering exploration into the electromagnetic field (EMF) responses from mycelium within a plant environment, utilizing a Hall effect sensor for detection. This project aims to uncover potential communication patterns or responses to environmental stimuli in plants, translated through EMF variations. The findings are visually represented through a dynamic LED light strip, reflecting the plant's condition via a color scale. This repository encompasses the entire workflow from data collection to advanced AI-driven analysis.

## Technical Description

The core of our setup includes a Hall effect sensor linked to a Raspberry Pi via an ADC (Analog-to-Digital Converter). The sensor readings capture the EMF responses from mycelium, which are then visualized through a color-mapped LED light strip. Data is streamed in real-time to Firebase, facilitating immediate web-based analysis and visualization.

### Components

- Hall effect sensor
- Analog-to-Digital Converter (ADC)
- Raspberry Pi
- LED light strip
- Firebase for data handling and real-time storage

## Installation and Setup

Follow the detailed instructions in the [Installation Guide](/EMFDataInsights/data_collection/EMFDataInsights_Setup_Guide.ipynb) to prepare your hardware and software setup. This includes configuring the Raspberry Pi, connecting the Hall effect sensor and LED strip, and setting up Firebase for data streaming.

## Usage

Comprehensive usage instructions are provided in the [Usage Guide](/EMFDataInsights/data_collection/readme.md), detailing steps to collect, transmit, and analyze data. Key scripts include:

- `sensor_readings.py`: Collects EMF data from the Hall effect sensor.
- `data_analysis.ipynb`: Analyzes the collected data with techniques like FFT.
- `visualization.html`: Facilitates real-time data visualization on the web.

## Data Visualization

Explore data visualization techniques and access the live data visualization platform in the [Visualizations](/EMFDataInsights/visualizations/readme.md) folder. This includes real-time graphs and analysis of EMF data, showcasing the responsive patterns of the plant to various stimuli.

## Analysis and Results

In-depth data analysis procedures, including FFT, gain control, and pattern identification, are documented within the [Analysis](/EMFDataInsights/data_analysis/readme.md) directory. This section elaborates on the patterns identified, interpreting their possible meanings, and discussing their relevance to plant communication theories.

## AI and Pattern Detection

The [AI Analysis](/EMFDataInsights/ai_analysis/readme.md) section delves into the application of machine learning algorithms for detecting patterns in EMF data. It provides an understanding of the algorithms used, the reasoning behind their selection, and the insights they offer into plant EMF signal patterns.

## Insights

Further exploration and interpretation of the AI-generated data can be found in the [Insights](/EMFDataInsights/insights/readme.md) folder. This includes a comprehensive analysis of how AI can be used to decipher complex EMF signal patterns, potentially representing mycelium "words" or communication methods.

## Replication and Contribution

Guidelines for replicating the study and contributing to the project are available, encouraging open collaboration and improvement. This includes a detailed list of materials, software setup instructions, and guidelines for contributing data or code enhancements.

## Reflections and Future Work

Reflections on the project's findings, challenges encountered, and strategies for overcoming them are discussed. This section also outlines potential avenues for future research and enhancements to the data collection and analysis methodologies.

## Acknowledgements

We extend our gratitude to all contributors and supporters who have played a pivotal role in advancing this project. Your insights, feedback, and encouragement have been invaluable.

