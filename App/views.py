from django.shortcuts import render
from .models import Location
import folium

def Folium_map(request):
    # Create a Folium map centered at a specific location with satellite imagery
    m = folium.Map(
        location=[45.5236, -122.6750],  # Coordinates for Portland, OR
        zoom_start=11,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri'
    )
    
    # Retrieve all locations from the database
    locations = Location.objects.all()
    
    # Add a marker for each location
    for location in locations:
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=location.name
        ).add_to(m)
    
    # Render the map in the template
    map_html = m._repr_html_()
    return render(request, 'index.html', {'map': map_html})