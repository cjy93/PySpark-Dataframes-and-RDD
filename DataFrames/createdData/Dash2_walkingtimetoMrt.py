# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import urllib.request
import json
import numpy as np
import dash_core_components as dcc


#Mapbox api
MAPBOX_TOKEN = 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# variables
fn = "C:/Users/jia yi/Desktop/NSDBA2/IT8703 Streaming analytics/ca1/Dataframe CA sol/createdData/MRT_estate_nearest_dist.csv"
df_fn = pd.read_csv(fn)

# Create a trace

# change this if you want tabs
from app import app
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change this if you want tabs
#app.layout = html.Div(children=[
layout = html.Div(children=[
    html.H1(children='Walking Distance to Mrt VS Percentage Sold',style ={'text-align': 'center'}),  

  
   dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'y': df_fn.walkingtime.tolist(),
                    'x': df_fn.percentagesold.tolist(),
                    'text': df_fn.project.tolist(),
                    'name': 'Trace 1',
                    'mode': 'lines+markers',
                    'marker': {'size': 12}
                },
               
            ],
            'layout': {
                'clickmode': 'event+select',
                'yaxis':{
                    'title': 'walking time in minutes to nearest MRT',
                },
                'xaxis':{
                    'title': 'Percentage sold',
                },
            }
        }
    ),

])

# ,style={'columnCount': 2}













if __name__ == '__main__':
    app.run_server(debug=True)





