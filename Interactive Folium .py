#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon

spacex_df=pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
spacex_df


# ## TASK 1 
# Add a new column called "marker_color". In this column input "red" for unsuccessful launch attempts and "green" for successful launch attempts.

# In[2]:


spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df

marker_color = ['red','green', 'green', 'red']
launch_sites_df['marker_color'] = marker_color
launch_sites_df


# ## TASK 2
# Map the location of the Nasa Johnson Space Center based on the center's coordinates. 

# In[2]:


nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)
site_map

circle = folium.Circle(nasa_coordinate, radius=1000, color='blue', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
marker = folium.map.Marker(nasa_coordinate, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))

site_map.add_child(circle)
site_map.add_child(marker)
site_map


# ## TASK 3
# Mark all launch sites on a map

# In[3]:


spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df

marker_color = ['red','green', 'green', 'red']
launch_sites_df['marker_color'] = marker_color
launch_sites_df

nasa_coordinate = [29.559684888503615, -95.0830971930759]
nasa_coordinate2 = [28.562302, -80.577356]
nasa_coordinate3 = [28.563197, -80.576820]
nasa_coordinate4 = [28.573255, -80.646895]
nasa_coordinate5 = [34.632834, -120.610745]

site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
site_map = folium.Map(location=nasa_coordinate2, zoom_start=5)
site_map = folium.Map(location=nasa_coordinate3, zoom_start=5)
site_map = folium.Map(location=nasa_coordinate4, zoom_start=5)
site_map = folium.Map(location=nasa_coordinate5, zoom_start=5)


circle = folium.Circle(nasa_coordinate, radius=1000, color='blue', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
circle2 = folium.Circle(nasa_coordinate2, radius=1000, color='yellow', fill=True)
circle3 = folium.Circle(nasa_coordinate3, radius=1000, color='green', fill=True)
circle4 = folium.Circle(nasa_coordinate4, radius=1000, color='red', fill=True)
circle5 = folium.Circle(nasa_coordinate5, radius=1000, color='purple', fill=True)

marker = folium.map.Marker(nasa_coordinate, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))
marker2 = folium.map.Marker(nasa_coordinate2, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))
marker3 = folium.map.Marker(nasa_coordinate3, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))
marker4 = folium.map.Marker(nasa_coordinate4, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))  
marker5 = folium.map.Marker(nasa_coordinate5, icon=DivIcon(icon_size=(20,20), icon_anchor=(0,0), html='<div style="font-size: 12; color:red;"><b>%s</b></div>' % 'NASA JSC',))

site_map.add_child(circle) 
site_map.add_child(circle2)
site_map.add_child(circle3)
site_map.add_child(circle4)
site_map.add_child(circle5)

site_map.add_child(marker)
site_map.add_child(marker2)
site_map.add_child(marker3)
site_map.add_child(marker4)
site_map.add_child(marker5)
site_map




# In[ ]:




