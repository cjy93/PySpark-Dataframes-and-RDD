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

fn_longlat = "C:/Users/jia yi/Desktop/NSDBA2/IT8703 Streaming analytics/ca1/Dataframe CA sol/createdData/forBubbleChart.csv"
df_fn = pd.read_csv(fn_longlat)

# for colour coding of bubbles
def colourCode(marketSegment):
    if marketSegment == "CCR":
        return('rgb(255,0,0)')
    elif marketSegment == "RCR":
        return('rgb(0,255,0)')
    else :
        return('rgb(0,0,255)')
        
# change this if you want tabs
from app import app
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change this if you want tabs
#app.layout = html.Div(children=[
layout = html.Div(children=[
    html.H1(children='Market Segmentation vs Median Price',style ={'text-align': 'center'}),  
    html.Div(children=[
        # drop down to top filters of unsold properties
        html.Br(),
        html.Label('Choose top how many unsold properties'),        
        dcc.Dropdown(
            id = 'topUnsold',
            options=[
                {'label':100, 'value':100},
                {'label':50, 'value':50},
                {'label':20, 'value':20},
                {'label':10, 'value':10},
                {'label':5, 'value':5},
            ],
            value = 20 # this value is initialise for districtNumber
        ),
        # drop down to choose district by name
        html.Br(),
        html.Label('Choose the available districts'),
        dcc.Dropdown(
            id = 'districtName2',
            options= [],
            #value = 1 # this value is initialise for districtNumber
        ),
        
        # output from drop down by district name is Project names
        html.Br(),
        html.Label('See here for the available projects based on districts'),
        dcc.Textarea(
            id = "Project2",
            placeholder='Project name displayed',
            value='This is a TextArea component',
            style={'width': '100%','height': '150px'}
        ),
    ], style= {'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    
    #html.Div(children='''
    #    Dash: A web application framework for Python.
    #'''),
    # map
    dcc.Graph(id='All_map2', style= {'width': '79%', 'display': 'inline-block'}), 
    html.Div(children='Core Central Region(CCR): Red , Rest of Central Region(RCR): Green , Outside Central Region(OCR):Blue',style ={'text-align': 'center'}),


])

# ,style={'columnCount': 2}





# interactive between choosing of districtName to output available Project names
@app.callback(
    dash.dependencies.Output('districtName2', 'options'),
    [   dash.dependencies.Input('topUnsold', 'value'),
        
    ],
    )
    
    # this func is for drawing Project. This comes as a pari with the above callback
def update_availableDistrict(selectedFilter):    
    print('asdsdsad :{}'.format(selectedFilter))
    df_selectedfilter = df_fn.head(selectedFilter)
    list_filtered_district = df_selectedfilter['District'].unique().tolist()
    print(type(list_filtered_district[0]))


    district_drop_options = []
    for row in dropdownlist.iterrows():
        district = row[1][0]
        districtName2 = row[1][2]
        if int(district) in list_filtered_district:
            print('True: {}'.format(district))
            dict_district = {'label': districtName2, 'value': district}
            district_drop_options.append(dict_district)
        else:
            print('False:{}'.format(type(district)))
    return(district_drop_options)
    
# interactive between choosing of districtName to output Project names
@app.callback(
    dash.dependencies.Output('Project2', 'value'),
    [   dash.dependencies.Input('districtName2', 'value'),
        dash.dependencies.Input('topUnsold', 'value'),
        
    ],
    )
    
    # this func is for drawing Project. This comes as a pari with the above callback
def update_project(selectedDistrictNum, selectedFilter):
    print(selectedDistrictNum, selectedFilter)
    if selectedDistrictNum is not None:
        df_filtered = df_fn[df_fn['District'] == int(selectedDistrictNum)]
        df_filtered2 = df_filtered.head(selectedFilter)
        a = df_filtered2.Project.tolist()
        aStr = '\n'.join(a)
    else:
        aStr = "No Project Found"
    print(aStr)
    return(aStr)




@app.callback(
    dash.dependencies.Output('All_map2', 'figure'),
    [   dash.dependencies.Input('districtName2', 'value'),
        dash.dependencies.Input('topUnsold', 'value'),
        
    ],
    )
    
    # the following are values from the above id
def update_map(selectedDistrictNum, selectedFilter):
    print(selectedDistrictNum, selectedFilter)
    if selectedDistrictNum is not None:
        df_filtered = df_fn[df_fn['District'] == int(selectedDistrictNum)]
        df_filtered2 = df_filtered.head(selectedFilter)
        long = df_filtered2.Longitude.tolist()
        lat = df_filtered2.Latitude.tolist() 
        medianPrice = df_filtered2.MediumPricePerSQFT.tolist()
        proj = df_filtered2.Project.tolist()
        colourCodeList = [colourCode(x) for x in df_filtered2['MarketSegment']]
        marketSegMent = df_filtered2.MarketSegment.tolist()
    # if no select then no action    
    else:
        long = []
        lat =[]
        medianPrice = []
        proj = []
        colourCodeList = []
        marketSegment = []
    #return(long,lat,proj)
   
    
    
    # layout of the map
    layout = go.Layout(
            mapbox= {
                'accesstoken': MAPBOX_TOKEN,
                'center': {'lat': 1.353869, 'lon':103.817780},
                'zoom': 10.5,
                'style': 'light'

            },
            hovermode = 'closest',
            margin = {'l': 0, 'r': 0, 'b': 0, 't': 20},
            #height=400, 
            #width=400,
    )


   
    dummyLat = lat
    dummyLong = long
    #dummyCustomData = ['block1','block2','block3']
    dummyHoverText = proj #, marketSegment





    return go.Figure(
            data=[
                go.Scattermapbox(
                    lat = dummyLat,
                    lon = dummyLong,
                    mode = 'markers',
                    marker = dict(
                        size= medianPrice*50,
                        opacity = 0.6,
                        reversescale = True,
                        autocolorscale = False,
                        color = colourCodeList,
                        
                        
                       
                        #colorbar = dict(
                        #    thickness = 10,
                        #    titleside = "top"
                        #),
                    ),
                    #customdata = dummyCustomData,
                    hoverinfo = 'text', 
                    hovertext = dummyHoverText,
                    name = 'NSL Mrt Station',
                ),
                
                

            ],
            layout=layout
    )






if __name__ == '__main__':
    app.run_server(debug=True)





