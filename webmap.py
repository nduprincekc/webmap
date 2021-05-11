import folium, pandas

# adding the volcanoes to the pandas library
data = pandas.read_csv('Volcanoes.txt')

# code for finding the latitude
lat = list(data['LAT'])

# code for finding the longititude
lon = list(data['LON'])

# code for finding the elevetion
ele = list(data['ELEV'])
map1 = folium.Map(location=[38.58, -99.09])
fg = folium.FeatureGroup(name='my map')


# color picker function
def color_picker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# grouping the volcanoes with the method feature group


fgv = folium.FeatureGroup(name='Volcanoes')


# looping through the latitude,longitude , elevation
for lt, ln, ele in zip(lat, lon, ele):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(ele) + ' m',
                                      fill_color=color_picker(ele), color='grey', fill_opacity=0.7))

# code for the population density
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'
                                                      }))

map1.add_child(fgp)
map1.add_child(fgv)
map1.add_child(folium.LayerControl())
map1.save('map1.html')
# print(data)
