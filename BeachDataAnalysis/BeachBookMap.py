import pandas as pd
import folium
from folium.plugins import HeatMap

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

# Iterate through each field to create heatmap layers
for field in fields:
    # Generate heatmap data considering max and max-1 values
    heat_data = [[row['Latitude'], row['Longitude'], 1]  # The '1' is a placeholder for intensity
                 for index, row in data.iterrows() if (row[field] == max_value_dict[field] or row[field] == max_value_dict[field] - 1) and not pd.isna(row['Latitude']) and not pd.isna(row['Longitude'])]

    if heat_data:  # Check if there is any data to display
        # Create a heatmap layer
        heat_layer = HeatMap(heat_data, show=False, name=field)  # Set show=False to not display the layer initially
        
        # Add the heatmap layer to the map
        m.add_child(heat_layer)
        
marker_group = folium.FeatureGroup(name='Markers', show=False)  # 'show=False' makes the group hidden by default


for index, row in data.iterrows():
    if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
        # HTML content for popup
        html_content = f"""
        <h4>Details: {row['Name']}</h4>  <!-- Replace 'Detail' with your actual detail column name -->
        <img src="{row['Image']}" alt="image" style="width:650px;">  <!-- Replace 'Image_URL' with your actual image URL column name -->
        """
        iframe = folium.IFrame(html_content, width=700, height=900)
        popup = folium.Popup(iframe, max_width=700)
        
        # Add marker with popup to the marker group
        folium.Marker([row['Latitude'], row['Longitude']], popup=popup).add_to(marker_group)

# Add the marker group to the map
m.add_child(marker_group)


# Add layer control to allow layer selection
folium.LayerControl().add_to(m)

# Save to HTML
m.save('heatmap.html')
