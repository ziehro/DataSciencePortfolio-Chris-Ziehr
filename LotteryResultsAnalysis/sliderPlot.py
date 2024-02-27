import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.dates as mdates

# Load data
df = pd.read_csv('raw.csv')  # Replace with your actual data path
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dropna()  # Ensure datetime format and drop NaT

# Calculate Win Percentage
df['Win Percentage'] = ((df['Money Out'] / df['Money In']) * 100) - 100

# Ensure there are no NaT or NaN in 'Date' after conversion
df = df.dropna(subset=['Date'])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(15, 6))
plt.subplots_adjust(bottom=0.25)

# Initial plot setup
initial_window = 30  # Days
start_date = df['Date'].min()
end_date = start_date + pd.Timedelta(days=initial_window)

# Plot function for initial and updates
def plot_data(start_date, end_date):
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    filtered_df = df.loc[mask]
    ax.clear()  # Clear existing lines

    # Ensure data is sorted by date for consistent plotting
    filtered_df = filtered_df.sort_values('Date')

    # Plot Moon Age Positive line
    ax.plot(filtered_df['Date'], filtered_df['Moon Age Positive'], 'b-', label='Moon Age Positive')

    # Plot win percentage as color-coded and size-coded markers
    for _, row in filtered_df.iterrows():
        win_percentage = row['Win Percentage']
        color = 'green' if win_percentage > 0 else 'red'
        size = np.clip(win_percentage, 10, 100)  # Adjust size scale as needed, ensure minimum size for visibility
        ax.scatter(row['Date'], row['Moon Age Positive'], color=color, s=size)
    
    # Update axis and format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    fig.canvas.draw_idle()  # Redraw the plot

# Initial plot
plot_data(start_date, end_date)

# Function to update the plot based on the slider value
def update(val):
    new_start_date_num = slider.val
    new_start_date = mdates.num2date(new_start_date_num)  # Convert from Matplotlib format to Python datetime
    new_start_date = pd.to_datetime(new_start_date).tz_localize(None)  # Convert to pandas timestamp and remove timezone
    new_end_date = new_start_date + pd.Timedelta(days=initial_window)
    plot_data(new_start_date, new_end_date)

# Set up the slider
axcolor = 'lightgoldenrodyellow'
axpos = plt.axes([0.125, 0.1, 0.775, 0.03], facecolor=axcolor)
slider = Slider(ax=axpos, label='Start Date', valmin=mdates.date2num(df['Date'].min()), valmax=mdates.date2num(df['Date'].max() - pd.Timedelta(days=initial_window)), valinit=mdates.date2num(start_date))
slider.on_changed(update)

# Show plot
plt.show()
