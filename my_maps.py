import folium
import pandas

my_map=folium.Map(location=[22.914377561511873,79.65930938145928],zoom_start=5,min_zoom=2.5,max_bounds=True)

volcano_read_data=pandas.read_csv('Volcano_Data.txt',sep=';')

vtype=volcano_read_data['type']
vlat=volcano_read_data['latitude']
vlon=volcano_read_data['longitude']
velev=volcano_read_data['elevation']
vname=volcano_read_data['name']

mountain_read_data=pandas.read_csv('Mountain_Data.txt',sep=';')
mtype=mountain_read_data['type']
mlat=mountain_read_data['latitude']
mlon=mountain_read_data['longitude']
melev=mountain_read_data['elevation']
mname=mountain_read_data['name']

def icon_filling(x):
    if int(x)<=2000:
        return 'green'
    elif int(x)>2000 and int(x)<=4000:
        return 'orange'
    elif int(x)>4000 and int(x)<=6000:
        return 'red'
    else:
        return 'blue'

volcano_icon=folium.features.CustomIcon('volcano.png',icon_size=(30,30))
mountain_icon=folium.features.CustomIcon('mountain.png',icon_size=(30,30))
layer1=folium.FeatureGroup(name='Volcanoes')
layer2=folium.FeatureGroup(name='Mountains')

for a,b,c,d in list(zip(vlat,vlon,velev,vname)):
    folium.Marker(location=[a,b],
                  popup=folium.Popup(html=f"<img src = 'volcano.png' style='width:25px;height:25px;'> <u>{str(c)} m</u>",max_width=100),
                  tooltip=f"<strong>{d}</strong>",
                  icon=folium.Icon(icon='flag',color=icon_filling(c))).add_to(layer1)

for p,q,r,s in list(zip(mlat,mlon,melev,mname)):
    folium.Marker(location=[p,q],
                  popup=folium.Popup(html=f"<img src = 'mountain.png' style='width:25px;height:25px;'> <u>{str(r)} m</u>",max_width=100),
                  tooltip=f"<strong>{s}</strong>",
                  icon=folium.Icon(icon='flag',color=icon_filling(r))).add_to(layer2)
my_map.add_child(layer1)
my_map.add_child(layer2)
my_map.add_child(folium.LayerControl())
my_map.save('Maps.html')