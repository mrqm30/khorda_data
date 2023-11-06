import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Define los datos de ejemplo para los gráficos
data_1 = px.data.iris()
data_2 = px.data.gapminder()
data_3 = px.data.tips()

# Define una función para crear un botón de redes sociales
def social_button(app, icon, text, button_id):
    return html.Div(
        className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-blue-300 to-blue-100 text-white-600 px-4 py-2 grid grid-cols-2",
        children=[
            html.Img(src=app.get_asset_url(icon), style={'width': '50px', 'height': '50px'}),
            html.Button(text, id=button_id, n_clicks=0, className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full m-2")
        ]
    )

# Define la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css'])
app.title = 'Analítica Social'

# Define el layout de la aplicación
app.layout = html.Div(
    className="mx-auto p-4",
    children=[
        html.Div(
            className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-5 gap-4",
            children=[
                html.Div(
                    className="bg-gray-100 p-4 col-span-4 sm:col-span-1 md:col-span-4 lg:col-span-4 xl:col-span-1 rounded-lg",
                    children=[
                        html.Div(
                            className="flex items-center justify-center",
                            children=[
                                html.Img(src=app.get_asset_url("carlos.jpeg"), style={'width': '200px', 'height': '200px', 'border-radius': '50%'}),
                            ]
                        ),
                        html.Br(),
                        html.H1("Carlos Lomelí Bolaños", className="text-center text-3xl font-bold leading-8 text-pink-600"),
                        html.H2("Gobernador 2024-2030", className="text-center text-3xl font-bold leading-8 text-pink-600"),
                        html.Br(),
                        social_button(app, 'tik-tok.png', 'TikTok', 'button-1'),
                        html.Br(),
                        social_button(app, 'x.png', 'Twitter', 'button-2'),
                        html.Br(),
                        social_button(app, 'youtube.png', 'YouTube', 'button-3'),
                        html.Br(),
                        social_button(app, 'facebook.png', 'Facebook', 'button-4'),
                        html.Br(),
                        social_button(app, 'instagram.png', 'Instagram', 'button-5'),
                        html.Br(),
                        dcc.Graph(id='social-graph')
                    ]
                ),
                html.Div(
                    className="bg-gray-100 p-4 col-span-4 md:col-span-4 lg:col-span-4 xl:col-span-4 rounded-lg",
                    children=[
                        html.Div(
                            className="grid gap-3 grid-cols-1 lg:grid-cols-3",
                            children=[
                                dcc.Graph(id="graph-1"),
                                dcc.Graph(id="graph-2"),
                                dcc.Graph(id="graph-3")
                            ]
                        ),
                        html.Br(),
                        html.Div(
                            className="grid gap-4 grid-cols-1 lg:grid-cols-4",
                            children=[
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-700 to-pink-900 text-white-900 px-4 py-2",
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
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-700 to-pink-900 text-white-900 px-4 py-2",
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
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-700 to-pink-900 text-white-900 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("pulgares-hacia-arriba.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Favoritos")
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="col-span-1 sm:col-span-1 xl:col-span-1",
                                    children=[
                                        html.Div(
                                            className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-lg bg-gradient-to-r from-pink-700 to-pink-900 text-white-900 px-4 py-2",
                                            children=[
                                                html.Img(src=app.get_asset_url("ojo.svg"), style={'width': '50px', 'height': '50px'}),
                                                html.H1("Alcance")
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Br(),
                        html.Div(
                            className="col-span-2 mt-5",
                            children=[
                                html.Div(
                                    className="grid gap-1 grid-cols-1 lg:grid-cols-2",
                                    children=[

                                    ]
                                )
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
    Output('social-graph', 'figure'),
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Input('button-1', 'n_clicks'),
    Input('button-2', 'n_clicks'),
    Input('button-3', 'n_clicks')
)
def update_graph(button1_clicks, button2_clicks, button3_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'button-1':
        figure = px.scatter(data_1, x='sepal_width', y='sepal_length', color='species')
    elif button_id == 'button-2':
        figure = px.scatter(data_2, x='gdpPercap', y='lifeExp', color='continent')
    elif button_id == 'button-3':
        figure = px.scatter(data_3, x='total_bill', y='tip', color='sex')
    else:
        figure = px.scatter(data_1, x='sepal_width', y='sepal_length', color='species')

    figure.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)'
    )

    return figure, figure, figure, figure

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
