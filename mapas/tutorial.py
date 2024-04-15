import folium 

""" 
m = folium.Map(location=(22.233113687134257, -97.86193249992799), tiles="cartodb positron", zoom_start=12)


folium.Marker(
    location=[22.216058633137134, -97.85752053544931],
    tooltip="Click!",
    popup="Plaza de armas Tampico",
    icon=folium.Icon(icon="green"),
).add_to(m)


m.save("index.html")

"""
import requests

m = folium.Map(tiles="cartodbpositron")

geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
).json()

folium.GeoJson(geojson_data, name="hello world").add_to(m)

folium.LayerControl().add_to(m)
m.save("index.html")
