
import os

import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

root_path = "C:/Users/pawel/Downloads/tiny-imagenet-200/test/images/"


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/Users/pawel/newfile15.txt')
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df.loc[:,'attr1'],
                    'y': df.loc[:,'attr2'],
                    'name': df.loc[:,'name'],
                    'text': ['a', 'b', 'c', 'd'],
                    'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                    'mode': 'markers',
                    'marker': {'size': 12}
                },
               
            ],
            'layout': {
                'clickmode': 'event+select'
            }
            
        }
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Div(id='hover-data', style=styles['pre'])
        ], className='three columns'),

        
       
        
    ])
])


@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    all_img_paths = df.loc[:,'name']
    img_nr = int(hoverData["points"][0]["pointIndex"])
    print(img_nr)
    return html.Img(src = os.path.join(root_path,all_img_paths[img_nr-1]))



if __name__ == '__main__':
    app.run_server(debug=False)