import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Define los datos de ejemplo para los gráficos
data_1 = px.data.iris()
data_2 = px.data.gapminder()
data_3 = px.data.tips()


external_stylesheets = ['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0, maximum-scale=3.0, minimum-scale=0.2"}])
app.language = 'es'
app.title = 'Analítica Social'

# Define el layout de la aplicación
app.layout = html.Div(
    className="mx-auto p-4",  # Agregué un padding general y altura mínima de pantalla completa
    children=[
        html.Div(
            className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-5 gap-4",
            children=[
                html.Div(
                    className="bg-gray-100 p-4 col-span-4 sm:col-span-1 md:col-span-4 lg:col-span-4 xl:col-span-1 rounded-lg",
                    children=[
                        html.Div(
                            className="flex items-center justify-center",  # Centrar horizontal y verticalmente
                            children=[
                                html.Img(src=app.get_asset_url("sasil.jpg"), style={'width': '200px', 'height': '200px', 'border-radius': '50%'}),
                            ]
                        ),
                        html.Br(),
                        html.H1("Sasil de León", className="text-center text-3xl font-bold leading-8 text-pink-600"),
                        html.H2("Gobernadora 2024", className="text-center text-3xl font-bold leading-8 text-pink-600"),
                        html.Br(),
                        # Botón 1
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
                            children=[
                                html.Img(src=app.get_asset_url('tik-tok.png'), style={'width': '50px', 'height': '50px'}),
                                html.Button("TikTok", id="button-1", n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
                            ]
                        ),
                        html.Br(),
                        # Botón 2
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
                            children=[
                                html.Img(src=app.get_asset_url("gorjeo.png"), style={'width': '50px', 'height': '50px'}),
                                html.Button("Twitter", id="button-2", n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
                            ]
                        ),
                        html.Br(),
                        # Botón 3
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
                            children=[
                                html.Img(src=app.get_asset_url("youtube.png"), style={'width': '50px', 'height': '50px'}),
                                html.Button("YouTube", id="button-3", n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
                            ]
                        ),
                        html.Br(),
                        # Botón 4
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
                            children=[
                                html.Img(src=app.get_asset_url("facebook.png"), style={'width': '50px', 'height': '50px'}),
                                html.Button("Facebook", id="button-4", n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
                            ]
                        ),
                        html.Br(),
                        # Botón 5
                        html.Div(
                            className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
                            children=[
                                html.Img(src=app.get_asset_url("instagram.png"), style={'width': '50px', 'height': '50px'}),
                                html.Button("Instagram", id="button-5", n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
                            ]
                        ),
                        html.Br(),
                        html.Div([
                            dcc.Graph()
                        ])
                    ]
                ),
                # Div de las gráficas
                html.Div(
                    className="bg-white-100 p-4 col-span-4 md:col-span-4 lg:col-span-4 xl:col-span-4 rounded-lg",
                    children=[
                        html.Div(
                            className="grid gap-3 grid-cols-1 lg:grid-cols-3",  # Alineación horizontal y separación entre elementos
                            children=[
                                html.Div(
                                    className="bg-gray-200 p-4 rounded-lg",
                                    children=[dcc.Graph(id="graph-1")]),
                                html.Div(
                                    className="bg-gray-200 p-4 rounded-lg",
                                    children=[dcc.Graph(id="graph-2")]),
                                html.Div(
                                    className="bg-gray-200 p-4 rounded-lg",
                                    children=[dcc.Graph(id="graph-3")]),
                                ]
                            ),
                        html.Br(),
                        # Cards de metrica
                        html.Div(
                            className="grid gap-4 grid-cols-1 lg:grid-cols-4",  # Cambiamos grid-cols a 4 para tener 4 columnas
                            children=[
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",  # Cada div hijo ocupa 25% del ancho en pantalla grande (lg)
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-500 to-pink-400 text-white-600 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("comentarios.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Comentarios")
                                                ]
                                            )
                                        ]
                                    ),
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-500 to-pink-400 text-white-600 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("flechas-repetir.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Reposts")
                                                ]
                                            )
                                        ]
                                    ),
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-500 to-pink-400 text-white-600 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("pulgares-hacia-arriba.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Like's")
                                                ]
                                            )
                                        ]
                                    ),
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-500 to-pink-400 text-white-600 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("ojo.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Vistas")
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                        html.Br(),
                        html.Div(
                            className="col-span-2 mt-5",  # Alineación horizontal y separación entre elementos
                            children=[
                                html.Div(
                                    className="grid gap-1 grid-cols-1 lg:grid-cols-2",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                            children=[
                                                dcc.Graph()
                                        ]),
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                            children=[
                                                dcc.Graph()
                                        ])
                                        ]),
                                ]
                            ),
                    ]
                )
            ]
        )

    ]
)

# Callback para generar gráficos diferentes en respuesta a los botones
@app.callback(
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Input('button-1', 'n_clicks'),
    Input('button-2', 'n_clicks'),
    Input('button-3', 'n_clicks')
)
def update_graph(button1_clicks, button2_clicks, button3_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identifica qué botón desencadenó la actualización

    if button_id == 'button-1':
        # Genera gráficos diferentes para cada dcc.Graph() en respuesta al botón 1
        figure_1 = px.scatter(data_1, x='sepal_width', y='sepal_length', color='species')
        figure_1.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_2 = px.bar(data_1, x='species', y='sepal_width')
        figure_2.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_3 = px.box(data_1, x='species', y='sepal_length')
        figure_3.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
    elif button_id == 'button-2':
        # Genera gráficos diferentes para cada dcc.Graph() en respuesta al botón 2
        figure_1 = px.scatter(data_2, x='gdpPercap', y='lifeExp', color='continent')
        figure_1.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_2 = px.bar(data_2, x='year', y='pop', color='continent')
        figure_2.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_3 = px.box(data_2, x='continent', y='lifeExp')
        figure_3.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
    elif button_id == 'button-3':
        # Genera gráficos diferentes para cada dcc.Graph() en respuesta al botón 3
        figure_1 = px.scatter(data_3, x='total_bill', y='tip', color='sex')
        figure_1.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_2 = px.bar(data_3, x='day', y='total_bill', color='sex')
        figure_2.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_3 = px.box(data_3, x='time', y='total_bill', color='sex')
        figure_3.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
    else:
        # Por defecto, muestra gráficos del botón 1
        figure_1 = px.scatter(data_1, x='sepal_width', y='sepal_length', color='species')
        figure_1.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_2 = px.bar(data_1, x='species', y='sepal_width')
        figure_2.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )
        figure_3 = px.box(data_1, x='species', y='sepal_length')
        figure_3.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
        )

    return figure_1, figure_2, figure_3


if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
