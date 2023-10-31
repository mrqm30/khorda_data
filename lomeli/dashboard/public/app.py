import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html, Output, Input

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

import plotly.graph_objects as go


external_stylesheets = ['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css']
# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1.0, maximum-scale=3.0, minimum-scale=0.2"}])
app.language = 'es'
app.title='Analitica Social'

app.layout = html.Div(
    className="mx-auto p-4",  # Agregué un padding general y altura mínima de pantalla completa
    children=[
        html.Div(
            className="container mx-auto",  # Centra el contenido en el medio de la pantalla
            children=[
                html.Div(
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4",
                    # Utiliza una cuadrícula flexible con 1 columna en dispositivos móviles, 2 en tablets, 3 en pantallas grandes y 5 en pantallas extra grandes
                    children=[
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 bg-pink-700 p-4 rounded-lg",  # Agregué un padding interno
                            children=[

                            ]
                        ),
                        html.Div(
                            className="bg-pink-700 p-4 rounded-lg",
                            children=[
                            ]
                        ),
                        html.Div(
                            className="bg-pink-700 p-4 rounded-lg",
                            children=[
                            ]
                        ),
                        html.Div(
                            className="bg-pink-700 p-4 rounded-lg",
                            children=[

                            ]
                        ),
                        html.Div(
                            className="bg-pink-700 p-4 rounded-lg",
                            children=[

                            ]
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
        html.Div(
            className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-5 gap-4 ",
            children=[
                html.Div(
                    className="bg-gray-100 p-4 col-span-1 md:col-span-1 lg:col-span-1 xl:col-span-1 rounded-lg",
                    children=[
                            html.H1(children='Title of Dash App'),
                            dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection')
                    ]
                    ),
                html.Div(
                    className="bg-gray-100 p-4 col-span-2 md:col-span-2 lg:col-span-2 xl:col-span-2 rounded-lg",
                    children=[
                        dcc.Graph(id='graph-content')
                        ]
                    ),
                html.Div(
                    className="bg-gray-100 p-4 col-span-2 md:col-span-2 lg:col-span-2 xl:col-span-2 rounded-lg",
                    children=[
                        dcc.Tabs(className="os-tab-container", id='tabs-example-1', value='tab-1', children=[
                            dcc.Tab(label='Posts', value='tab-1', className = 'os-tab'),
                            dcc.Tab(label='Comentarios', value='tab-2', className='os-tab'),
                            dcc.Tab(label='Hashtags', value='tab-3', className='os-tab'),
                            ]),
                        html.Div(id='tabs-example-content-1')
                        ]
                    ),
            ]
            )
    ]
)

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    fig = px.line(dff, x='year', y='pop')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)