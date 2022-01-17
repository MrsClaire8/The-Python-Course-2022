from branca.element import IFrame
import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])
name = list(data["NAME"])

def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map=folium.Map(location=[40, -110], zoom_start=6, tiles='Stamen Terrain')

fgv=folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln],
        stroke=False,
        radius=8,
        popup=folium.Popup(iframe),
        #popup=nm + ' ' + str(el) + ' m', parse_html=True,
        tooltip='Click me now',
        fill_opacity=0.7,
        fill_color=color(el)))

fgp=folium.FeatureGroup('Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save('map.html')