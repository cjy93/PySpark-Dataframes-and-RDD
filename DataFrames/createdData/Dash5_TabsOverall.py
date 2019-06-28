import dash
import dash_html_components as html
import dash_core_components as dcc
import Dash1_districtVsAttractiveness
import Dash2_walkingtimetoMrt
import Dash3_bubbleChartmarketSegment
import Dash4_Rental_vs_Developer_InSameRegion
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# change this
from app import app
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='District impact on Attractiveness', value='tab-1'),
        dcc.Tab(label='Walking Time to MRT vs Price', value='tab-2'),
        dcc.Tab(label='Bubble Chart Market Segments', value='tab-3'),
        dcc.Tab(label='Rental vs DeveloperSales', value='tab-4'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return Dash1_districtVsAttractiveness.layout # layout is the variable in Dash1, Dash2,... as a variable
        #    html.H3('Tab content 1')
        #])
    elif tab == 'tab-2':
        return Dash2_walkingtimetoMrt.layout
        
    elif tab == 'tab-3':
        return Dash3_bubbleChartmarketSegment.layout
    elif tab == 'tab-4':
        return Dash4_Rental_vs_Developer_InSameRegion.layout


if __name__ == '__main__':
    app.run_server(debug=True)