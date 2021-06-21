import pandas as pd
import geopandas as gpd
import osmnx as ox
import folium
import matplotlib.pyplot as plt
import seaborn as sns

## Streets
place = "Liverpool, United Kingdom"
graph = ox.graph_from_place(place, network_type='drive')

print(len(graph))

nodes, streets = ox.graph_to_gdfs(graph)

nodes.head()

streets.head()

street_types = pd.DataFrame(streets["highway"].apply(pd.Series)[0].value_counts().reset_index())
street_types.columns = ["type", "count"]

fig, ax = plt.subplots(figsize=(12,10))
sns.barplot(y="type", x="count", data=street_types, ax=ax)
plt.tight_layout()
plt.savefig("barchart.png")

style = {'color': '#F7DC6F', 'weight':'1'}
m = folium.Map([-2.914018, 53.366925],
               zoom_start=15,
               tiles="CartoDb dark_matter")
folium.GeoJson(streets, style_function=lambda x: style).add_to(m)
m.save("streets.html")

## Building footprints
buildings = ox.geometries_from_place(place, tags={'building':True})
print(buildings.head())

print(buildings.shape)

cols = ['amenity','building', 'name', 'tourism']
print(buildings[cols].head())

#list(buildings.columns)
#buildings["amenity"].apply(pd.Series)[0].value_counts()

style_buildings = {'color':'#6C3483 ', 'fillColor': '#6C3483 ', 'weight':'1', 'fillOpacity' : 1}

m = folium.Map([53.366925, -2.914018],
               zoom_start=15,

               tiles="Stamen Toner")

folium.GeoJson(buildings[:1000], style_function=lambda x: style_buildings).add_to(m)
m.save("buildings.html")

## Points of interests - Cafes
tags = {'amenity': 'cafe'}
cafe = ox.geometries_from_place(place, tags)
cafe = cafe.reset_index(level=['osmid'])
print(cafe.head())
print(cafe.shape)
print(cafe.columns)

columns=['osmid','name','wheelchair','opening_hours','addr:street','addr:city','addr:postcode']
cafe[columns].head()
cafe_points=cafe[cafe.geom_type=="Point"]

m = folium.Map([53.366925, -2.914018], zoom_start=10, tiles="CartoDb dark_matter")
locs = zip(cafe_points.geometry.y, cafe_points.geometry.x)
#folium.GeoJson(buildings, style_function=lambda x: style_buildings).add_to(m)
for location in locs:
    folium.CircleMarker(location=location,
        color = "#F4F6F7",   radius=2).add_to(m)
m.save("cafes.html")

print(cafe['geometry'])
