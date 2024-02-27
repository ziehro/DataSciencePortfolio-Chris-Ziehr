# Lottery Results Analysis

This project analyzes the relationship between the moon phases and lottery win percentages. Utilizing data on lottery results and corresponding moon ages, we investigate patterns and correlations to understand how the lunar cycle might influence lottery outcomes.

## Files

- `raw.csv`: This file contains the raw data used for the analysis. It includes dates, moon ages, money spent, money won, and calculated win percentages for each recorded day.

- `Interactive_Moon_Phase_Analysis.ipynb`: Jupyter notebook containing all the code and visualizations for the analysis. The notebook includes data preprocessing, feature engineering, and an interactive graph that displays the moon phase as a continuous sine wave, with overlaying data points representing the win percentages for corresponding days.

## How to Use

1. Clone this repository or download the files to your local machine.
2. Ensure you have Jupyter Notebook or JupyterLab installed to run the `.ipynb` file. You can install it via Anaconda or with pip using the command `pip install notebook`.
3. Open `Interactive_Moon_Phase_Analysis.ipynb` in Jupyter Notebook or JupyterLab.
4. Run all the cells in the notebook to reproduce the analysis and visualizations. The notebook contains comments and markdown cells that guide you through the process.

## Interactive Graph Features

The main feature of this analysis is the interactive graph which displays:
- A continuous sine wave representing the moon phase over time.
- Data points overlaying the sine wave to represent win percentages for respective days.
- The ability to scroll horizontally through the dates to view different segments of time within the 30-day window.
- Colors and sizes of the data points vary based on the win percentage, providing a quick visual interpretation of the data.

## Requirements

- Python 3.x
- Libraries: pandas, numpy, matplotlib, matplotlib.widgets

## Acknowledgements

This analysis was inspired by the hypothesis that lunar cycles may impact human behavior and, by extension, lottery outcomes. The methodology and visualizations were developed to provide a clear and interactive way to explore this potential relationship.
