#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
spacex_df

spacex_df['Launch Site'].unique()


# In[ ]:


import pandas as pd
import plotly.graph_objects as go 
import dash
import plotly.express as px
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
    dcc.Dropdown(id='site-dropdown', options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},], value='ALL', placeholder='Select a Launch Site here', searchable=True),                                             
    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, marks={0: '0', 100: '100'}, value=[min_payload, max_payload]),                               
        html.Div(dcc.Graph(id='success-payload-scatter-chart')),])

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
              

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', 
        names='Launch Site', 
        title='Successful Count for all launch sites')
        return fig
    else:
        filtered_df=spacex_df[spacex_df['Launch Site']== entered_site]
        filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')
        fig=px.pie(filtered_df,values='class count',names='class',title=f"Total Success Launches for site {entered_site}")
        return fig
              
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='payload-slider', component_property='value'))


def get_scatter(entered_site,payload):
    filtered_df2_1=spacex_df[(spacex_df['Payload Mass (kg)'] > payload[0]) & (spacex_df['Payload Mass (kg)'] < payload[1])]

    if entered_site =='ALL':
        fig= px.scatter(filtered_df2_1,x="Payload Mass (kg)",y="class",color="Booster Version Category",\
        title="Correlation between Payload and Success for All sites")
        return fig
    else :
        filtered_df2_2=filtered_df2_1[filtered_df2_1['Launch Site']== entered_site]
        fig= px.scatter(filtered_df2_2,x="Payload Mass (kg)",y="class",color="Booster Version Category",\
        title=f"Correlation between Payload and Success for site {entered_site}")
        return fig

        if __name__ == '__main__':
            app.run_server()



