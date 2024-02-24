import pandas as pd
import folium
from folium.plugins import HeatMap, Fullscreen

# Load data
data = pd.read_csv('data.csv')

average_lat = data['Latitude'].mean()
average_lon = data['Longitude'].mean()

max_values = [7, 7, 5, 7, 7, 5, 9, 5, 5, 0, 7, 5, 5, 7, 7, 5, 5, 5, 7, 5]  # Max values for each field
fields = ['Anemones', 'Barnacles', 'Boulders', 'Bugs', 'Clams', 'Firewood', 'Garbage', 'Islands', 'Kindling', 'Limpets', 'Logs', 'Midden', 'Mussels', 'Oysters', 'Pebbles', 'Rocks', 'Sand', 'Snails', 'Stone', 'Trees']

# Mapping fields to their max values
max_value_dict = dict(zip(fields, max_values))


# Initialize map
m = folium.Map(location=[average_lat, average_lon], zoom_start=5)

# Add fullscreen control to the map
Fullscreen().add_to(m)

# Add title and description
title_html = """
             <h3 align="center" style="font-size:20px"><b>Beach Data Heatmap</b></h3>
             <p align="center" style="font-size:16px">Hover over the layers icon on the top right corner to select the data field to visualize. Enable 'Markers' for more information about the locations.</p>
             """

m.get_root().html.add_child(folium.Element(title_html))


# Iterate through each field to create heatmap layers
for field in fields:
    # Calculate the threshold as 40% of the maximum value for the field
    threshold = 0.5* max_value_dict[field]
    
    # Generate heatmap data, filtering based on the field value being >= threshold
    heat_data = [[row['Latitude'], row['Longitude'], 1]  # The '1' is a placeholder for intensity
                 for index, row in data.iterrows() if row[field] >= threshold]

    if heat_data:  # Check if there is any data to display
        # Create a heatmap layer
        heat_layer = HeatMap(heat_data, show=False, name=field)  # Set show=False to not display the layer initially
        
        # Add the heatmap layer to the map
        m.add_child(heat_layer)
        
marker_group = folium.FeatureGroup(name='Markers', show=False)  # 'show=False' makes the group hidden by default


for index, row in data.iterrows():
    if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
        # Construct additional details as an HTML list (you can format this as needed)
        details_html = ''.join([f'<li><b>{field}:</b> {row[field]}</li>' for field in fields])

        # Create HTML content for popup with expandable details using details and summary tags
        html_content = f"""
        <h3>{row['Name']}</h3>
        <p><b>Description:</b> {row['Description']}</p>
        <p><b>Timestamp:</b> {row['Timestamp']}</p>
        <p><b>Click for full image:</b><br>
        <a href="{row['Image']}" target="_blank"><img src="{row['Thumbnail']}" alt="image" style="width:100%; max-width:100px;"></a></p>
        <details>
            <summary>Show more details</summary>
            <ul>{details_html}</ul>
        </details>
        """

        # Create a popup with HTML content
        popup = folium.Popup(html_content, max_width=300)

        # Create a marker with popup
        marker = folium.Marker([row['Latitude'], row['Longitude']], popup=popup)

        # Add marker to the marker group
        marker.add_to(marker_group)



# Add the marker group to the map
m.add_child(marker_group)


# Add layer control to allow layer selection
folium.LayerControl().add_to(m)

# Save to HTML
m.save('heatmap.html')
