import folium


def generate_map():
    position = [55.757329957053166, 60.70401994075724]
    folium_map = folium.Map(location=position, zoom_start=16, tiles="OpenStreetMap")
    folium.Marker(position, popup="Школа 27", icon=folium.Icon(color='gray')) \
        .add_to(folium_map)
    folium_map.save('../../../templates/map.html')


generate_map()
