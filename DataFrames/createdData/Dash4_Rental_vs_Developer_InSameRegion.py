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

# to fetch api from Here.com
urlBase = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=CqnyNhJQRmXS5JggWAos&app_code=qsE9fGn1RRAPNOxzG1OeFA&waypoint0=geo!{}&waypoint1=geo!{}&mode=fastest;car;traffic:disabled'


#Mapbox api
MAPBOX_TOKEN = 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# variables
fn = "C:/Users/jia yi/Desktop/NSDBA2/IT8703 Streaming analytics/ca1/Dataframe CA sol/extra data/district_to_Postal.csv"
dropdownlist = pd.read_csv(fn)

fn_longlat = "C:/Users/jia yi/Desktop/NSDBA2/IT8703 Streaming analytics/ca1/Dataframe CA sol/createdData/developerRentalPrice.csv"
df_fn = pd.read_csv(fn_longlat)


        
# change this if you want tabs
from app import app
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change this if you want tabs
#app.layout = html.Div(children=[
layout = html.Div(children=[
    html.H1(children='Rental vs DeveloperSales in same location',style ={'text-align': 'center'}),  
    html.Div(children=[
        # drop down to top filters of unsold properties
        html.Br(),
        html.Label('Choose top how many unsold properties'),        
        dcc.Dropdown(
            id = 'topUnsold',
            options=[
                {'label':"All", 'value': len(df_fn)},
                {'label':100, 'value':100},
                {'label':50, 'value':50},
                {'label':20, 'value':20},
                {'label':10, 'value':10},
                {'label':5, 'value':5},
            ],
            value = 20 # this value is initialise for districtNumber
        ),
        
        # output from drop down by district name is Project names
        html.Br(),
        html.Label('See here for the available projects based on districts'),
        dcc.Textarea(
            id = "Project4",
            placeholder='Project name displayed',
            value='This is a TextArea component',
            style={'width': '100%','height': '150px'}
        ),
    ], style= {'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    
    #html.Div(children='''
    #    Dash: A web application framework for Python.
    #'''),
    
    # Scatter plot
    dcc.Graph(
        id='StreetVSPrice',
        
    ),
    html.Div()

])

# ,style={'columnCount': 2}





    
# interactive between choosing of districtName to output Project names
@app.callback(
    dash.dependencies.Output('Project4', 'value'),
    [ dash.dependencies.Input('topUnsold', 'value'),
        
    ],
    )
    
    # this func is for drawing Project. This comes as a pari with the above callback
def update_project(selectedFilter):
    print(selectedFilter)
    if selectedFilter is not None:
        df_filtered2 = df_fn.head(selectedFilter)
        a = df_filtered2.Project_y.tolist()
        print(a)
        
        stringname = ""
        for projectname in a:
            stringname = '{} \n {}'.format(stringname,projectname)
            
        
    else:
        stringname = "No Project Found"
    print(stringname)
    return(stringname)
    
# interactive between top how many to the scatter
@app.callback(
    dash.dependencies.Output('StreetVSPrice', 'figure'),
    [ dash.dependencies.Input('topUnsold', 'value'),
        
    ],
    )
    
    # this func is for drawing Project. This comes as a pari with the above callback
def update_scatter(selectedFilter):
    print(selectedFilter)
    if selectedFilter is not None:
        df_filtered2 = df_fn.head(selectedFilter)
        x = df_filtered2.Street
        y1= df_filtered2.PricePerSqft
        y2= df_filtered2.MediumPricePerSQFT
        name1= df_filtered2.Project_y
        name2= df_filtered2.Project_x
        
    else:
        x = []
        y1= []
        y2= []
        name1=[]
        name2=[]
   
    return go.Figure(
                data=[
                    go.Scatter(
                    x=x,
                    y=y1,
                    text=name1,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name= "Rental"
                ),
                go.Scatter(
                    x=x,
                    y=y2,
                    text=name2,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name= "Developer Sales"
                )
            ],
            layout= {
                'height': 500,
                'margin': {
                    'l': 10, 'b': 200, 't': 0, 'r': 0
                } # margin b is bottom
            }
        )







if __name__ == '__main__':
    app.run_server(debug=True)






