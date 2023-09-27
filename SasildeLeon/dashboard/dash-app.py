import dash
import re 
from io import BytesIO
import base64
import networkx as nx
import gensim
from gensim import corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
from wordcloud import WordCloud
import io
import random
from dash.dependencies import Input, Output
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
###Diccionarios en español para el análisis de polaridad
nltk.download('punkt')
# Tokenización
# Descargar el conjunto de stopwords en español si no lo tienes
nltk.download('stopwords')
# Análisis de polaridad
# Obtención de listado de stopwords del inglés
stop_words = list(stopwords.words('spanish'))
####################
import plotly.io as pio

pio.templates['new_template'] = go.layout.Template()
pio.templates['new_template']['layout']['font'] = {'family': 'verdana', 'size': 16, 'color': 'black'}
pio.templates['new_template']['layout']['paper_bgcolor'] = '#e5e7eb'
pio.templates['new_template']['layout']['plot_bgcolor'] = '#e5e7eb'
pio.templates['new_template']['layout']['xaxis'] = {'title_standoff': 10, 'linecolor': 'black', 'mirror': True, 'gridcolor': '#EEEEEE'}
pio.templates['new_template']['layout']['yaxis'] = {'title_standoff': 10, 'linecolor': 'black', 'mirror': True, 'gridcolor': '#EEEEEE'}
pio.templates['new_template']['layout']['legend_bgcolor'] = '#e5e7eb'
pio.templates['new_template']['layout']['height'] = 400
pio.templates['new_template']['layout']['width'] = 800
pio.templates['new_template']['layout']['autosize'] = False

pio.templates.default = 'new_template'

##################################DATA#############################
ts_cleaned = pd.read_csv("ts.csv")
tweets_tidy = pd.read_csv("tweets_tidy.csv")
top_words = pd.read_csv("top_words.csv")
top_words_coments_twitter = pd.read_csv("top_words_coments_twitter.csv")
tweets_posts_sentiment = pd.read_csv("tweets_posts_sentiment.csv")
tweets_coments_sentiment = pd.read_csv("tweets_coments_sentiment.csv")
##########################################################################
#tiktok 
tiktok_sentiment_posts = pd.read_csv("tiktok_sentiment_posts.csv")
tiktok_sentiment_coments = pd.read_csv("tiktok_sentiment_coments.csv")
tiktok_words_posts = pd.read_csv("tiktok_words_posts.csv")
tiktok_words_coments = pd.read_csv("tiktok_words_coments.csv")
######################################################################
#insta


insta_words_posts = pd.read_csv("insta_words_posts.csv")
####################################################################################################
external_stylesheets = ['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css']
# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1.0, maximum-scale=3.0, minimum-scale=0.2"}])
app.language = 'es'
app.title='Analitica Social'
# Carpeta donde se encuentran los iconos
icons_directory = "icons/"
# Definir las opciones del dropdown
opciones = [
    {'label': 'Empresa', 'value': 'Empresa'},
    {'label': 'Región', 'value': 'Region'},
    {'label': 'Área', 'value': 'Area'},
    {'label': 'Posición', 'value': 'Posicion'}
]
# Estilo de Tailwind CSS y color de fondo
app.layout = html.Div(
        className="mx-auto p-6 bg-[#F8F0E5]",
        #style={'background-color': '#F8F0E5'},
        children=[
            html.Div(
            #Inicio KPI's
            className="grid grid-cols-10 gap-6 mt-5",
            children=[
                #KPI 1: TikTok
                html.Div(
                    className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-pink-700 to-pink-600 text-white-600 px-4 py-2 grid grid-cols-2",
                    children=[
                        html.Div(
                            className="col-span-1",  # Ocupa la mitad del ancho 
                            children=[
                                html.Div(
                                    children=[
                                        html.Img(src=app.get_asset_url('tik-tok.png'), style={'width': '50px', 'height': '50px'}),
                                        html.H1("TikTok", className="text-3xl font-bold leading-8 text-white")
                                        ]
                                    )
                                ]
                            ),
                        html.Div(
                            className="col-span-1",  # Ocupa la otra mitad del ancho 
                            children=[
                                html.Div([
                                    html.H2("Vistas=4371", className="text-lg font-bold text-white"),
                                    html.H2("Likes=194", className="text-lg font-bold text-white"),
                                    html.H2("Repost=7", className="text-lg font-bold text-white"),
                                    html.H2("Comments=15", className="text-lg font-bold text-white"),
                                    ])
                                ]
                            )
                        ]
                    ),
                #KPI 2:Twitter
                html.Div(
                    className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-pink-700 to-pink-600 text-white-600 px-4 py-2 grid grid-cols-2",
                    children=[
                        html.Div(
                            className="col-span-1",  # Ocupa la mitad del ancho 
                            children=[
                                html.Div(
                                    children=[
                                        html.Img(src=app.get_asset_url("gorjeo.png"), style={'width': '50px', 'height': '50px'}),
                                        html.H1("Twitter", className="text-3xl font-bold leading-8 text-white")
                                        ]
                                    )
                                ]
                            ),
                        html.Div(
                            className="col-span-1",  # Ocupa la otra mitad del ancho 
                            children=[
                                html.Div([
                                    html.H2("Vistas = 326 mil", className="text-lg font-bold text-white"),
                                    html.H2("Likes = 129", className="text-lg font-bold text-white"),
                                    html.H2("Repost = 62", className="text-lg font-bold text-white"),
                                    html.H2("Comments = 55", className="text-lg font-bold text-white"),
                                    ])
                                ]
                            )
                        ]
                    ),
                #KPI 3:Youtube
                html.Div(
                    className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-pink-700 to-pink-600 text-white-600 px-4 py-2 grid grid-cols-2",
                    children=[
                        html.Div(
                            className="col-span-1",  # Ocupa la mitad del ancho 
                            children=[
                                html.Div(
                                    children=[
                                        html.Img(src=app.get_asset_url("youtube.png"), style={'width': '50px', 'height': '50px'}),
                                        html.H1("YouTube", className="text-3xl font-bold leading-8 text-white")
                                        ]
                                    )
                                ]
                            ),
                        html.Div(
                            className="col-span-1",  # Ocupa la otra mitad del ancho 
                            children=[
                                html.Div([
                                    html.H2("Vistas", className="text-lg font-bold text-white"),
                                    html.H2("Likes", className="text-lg font-bold text-white"),
                                    html.H2("Repost", className="text-lg font-bold text-white"),
                                    html.H2("Comments", className="text-lg font-bold text-white"),
                                    ])
                                ]
                            )
                        ]
                    ),
                #KPI 4:Facebook
                html.Div(
                    className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-pink-700 to-pink-600 text-white-600 px-4 py-2 grid grid-cols-2",
                    children=[
                        html.Div(
                            className="col-span-1",  # Ocupa la mitad del ancho 
                            children=[
                                html.Div(
                                    children=[
                                        html.Img(src=app.get_asset_url("facebook.png"), style={'width': '50px', 'height': '50px'}),
                                        html.H1("Facebook", className="text-3xl font-bold leading-8 text-white")
                                        ]
                                    )
                                ]
                            ),
                        html.Div(
                            className="col-span-1",  # Ocupa la otra mitad del ancho 
                            children=[
                                html.Div([
                                    html.H2("Vistas", className="text-lg font-bold text-white"),
                                    html.H2("Likes", className="text-lg font-bold text-white"),
                                    html.H2("Repost", className="text-lg font-bold text-white"),
                                    html.H2("Comments", className="text-lg font-bold text-white"),
                                    ])
                                ]
                            )
                        ]
                    ),
                #KPI 5:Instagram
                html.Div(
                    className="transform  hover:scale-105 transition duration-300 shadow-2xl rounded-lg col-span-12 sm:col-span-1 xl:col-span-2 intro-y bg-gradient-to-r from-pink-700 to-pink-600 text-white-600 px-4 py-2 grid grid-cols-2",
                    children=[
                        html.Div(
                            className="col-span-1",  # Ocupa la mitad del ancho 
                            children=[
                                html.Div(
                                    children=[
                                        html.Img(src=app.get_asset_url("instagram.png"), style={'width': '50px', 'height': '50px'}),
                                        html.H1("Instagram", className="text-3xl font-bold leading-8 text-white")
                                        ]
                                    )
                                ]
                            ),
                        html.Div(
                            className="col-span-1",  # Ocupa la otra mitad del ancho 
                            children=[
                                html.Div([
                                    html.H2("Vistas", className="text-lg font-bold text-white"),
                                    html.H2("Likes", className="text-lg font-bold text-white"),
                                    html.H2("Repost", className="text-lg font-bold text-white"),
                                    html.H2("Comments", className="text-lg font-bold text-white"),
                                    ])
                                ]
                            )
                        ]
                    )
            ]
        ),
        #Fin KPI's
        html.Br(),
        html.Div(
                className="col-span-5 mt-5",
                children=[
                    html.Div(
                        className="grid gap-2 grid-cols-1 lg:grid-cols-3",
                        children=[
                            html.Div(className="transform hover:scale-102 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
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
                                         dcc.Dropdown(['Twitter', 'TikTok', 'Instagram', 'YouTube'], 'Twitter', id='opcion-selector')]),
                            html.Div(className="transform hover:scale-102 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[dcc.Graph(id="graph_sentiment_posts", config={'displaylogo': False, 'responsive': True})]
                                     ),
                            html.Div(className="transform hover:scale-102 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[dcc.Graph(id="graph_sentiment_coments", config={'displaylogo': False, 'responsive':True})]
                                     ),
                            ])
                        ]),
        html.Br(),
        html.Div(
                className="col-span-5 mt-5",
                children=[
                    html.Div(
                        className="grid gap-2 grid-cols-1 lg:grid-cols-2",
                        children=[
                            html.Div(className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[
                                         dcc.Graph(id="graph_words", config={'displaylogo':False, 'responsive':True})

                                         ]),
                            html.Div(className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[dcc.Graph(id="graph_words_coments", config={'displaylogo':False, 'responsive':True})]
                                     ),
                            html.Div(className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[
                                         html.H2("Nube de palabras"),
                                         html.Img(src=app.get_asset_url("nube_palabras.png"))
                                         ]
                                     ),
                            html.Div(className="transform hover:scale-105 transition duration-300 shadow-2xl rounded-xl bg-gray-200 p-4",
                                     children=[
                                         html.Img(src=app.get_asset_url("topicos.png"))
                                         ]
                                     )
                            ])
                        ])
    ]
)


##########################################################################################
# Callback para actualizar el gráfico en función de la opción seleccionada
@app.callback(
        Output("graph_sentiment_posts", "figure"),
        Input("opcion-selector", "value"))
    
def update_graph(selector):
    if selector == 'Twitter':
        ####################################
        # Contar la cantidad de sentimientos negativos, neutros y positivos
        negativos = tweets_posts_sentiment[tweets_posts_sentiment["sentimiento"] < 0].count().values[0]
        neutros = tweets_posts_sentiment[tweets_posts_sentiment["sentimiento"] == 0].count().values[0]
        positivos = tweets_posts_sentiment[tweets_posts_sentiment["sentimiento"] > 0].count().values[0]

        # Crear la gráfica de pastel
        labels = ["Negativos", "Neutros", "Positivos"]
        values = [negativos, neutros, positivos]

        #fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        # Crear la figura de pastel con formato personalizado
        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Establecer el radio del hoyo en 0.5 para crear un hoyo en el medio
        pull=[0.1, 0.1, 0.1],  # Separar las porciones del pastel
        textinfo='label+percent',  # Mostrar etiquetas y porcentajes en la leyenda
        marker=dict(colors=['#1f77b4', '#be00c7', '#2ca02c']),  # Colores personalizados
        direction='counterclockwise',  # Dirección de rotación del pastel
        sort=False  # Desactivar la clasificación automática de las porciones
        )])

        # Actualizar el diseño de la figura
        fig.update_layout(
        title='Análisis de Polaridad en los posts',  # Establecer el título
        legend=dict(orientation='h', yanchor='bottom', y=-0.2),  # Colocar la leyenda debajo
        template='new_template'  # Utilizar el tema 'plotly_white'
        )

        return fig 

    elif selector == 'TikTok':
        ####################################
        # Contar la cantidad de sentimientos negativos, neutros y positivos
        negativos = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] < 0].count().values[0]
        neutros = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] == 0].count().values[0]
        positivos = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] > 0].count().values[0]

        # Crear la gráfica de pastel
        labels = ["Negativos", "Neutros", "Positivos"]
        values = [negativos, neutros, positivos]

        #fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        # Crear la figura de pastel con formato personalizado
        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Establecer el radio del hoyo en 0.5 para crear un hoyo en el medio
        pull=[0.1, 0.1, 0.1],  # Separar las porciones del pastel
        textinfo='label+percent',  # Mostrar etiquetas y porcentajes en la leyenda
        marker=dict(colors=['#1f77b4', '#be00c7', '#2ca02c']),  # Colores personalizados
        direction='counterclockwise',  # Dirección de rotación del pastel
        sort=False  # Desactivar la clasificación automática de las porciones
        )])

        # Actualizar el diseño de la figura
        fig.update_layout(
        title='Análisis de Polaridad en los posts',  # Establecer el título
        legend=dict(orientation='h', yanchor='bottom', y=-0.2),  # Colocar la leyenda debajo
        template='new_template'  # Utilizar el tema 'plotly_white'
        )

        return fig 



@app.callback(
        Output("graph_sentiment_coments", "figure"),
        Input("opcion-selector", "value"))

def update_graph(selector):
    if selector == 'Twitter':
        ####################################
        # Contar la cantidad de sentimientos negativos, neutros y positivos
        negativos = tweets_coments_sentiment[tweets_coments_sentiment["sentimiento"] < 0].count().values[0]
        neutros = tweets_coments_sentiment[tweets_coments_sentiment["sentimiento"] == 0].count().values[0]
        positivos = tweets_coments_sentiment[tweets_coments_sentiment["sentimiento"] > 0].count().values[0]

        # Crear la gráfica de pastel
        labels = ["Negativos", "Neutros", "Positivos"]
        values = [negativos, neutros, positivos]

        #fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        # Crear la figura de pastel con formato personalizado
        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Establecer el radio del hoyo en 0.5 para crear un hoyo en el medio
        pull=[0.1, 0.1, 0.1],  # Separar las porciones del pastel
        textinfo='label+percent',  # Mostrar etiquetas y porcentajes en la leyenda
        marker=dict(colors=['#1f77b4', '#be00c7', '#2ca02c']),  # Colores personalizados
        direction='counterclockwise',  # Dirección de rotación del pastel
        sort=False  # Desactivar la clasificación automática de las porciones
        )])

        # Actualizar el diseño de la figura
        fig.update_layout(
        title='Análisis de Polaridad en los comentarios',  # Establecer el título
        legend=dict(orientation='h', yanchor='bottom', y=-0.2),  # Colocar la leyenda debajo
        template='new_template'  # Utilizar el tema editado arriba
        )

        return fig

    elif selector == 'TikTok':
        ####################################
        # Contar la cantidad de sentimientos negativos, neutros y positivos
        negativos = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] < 0].count().values[0]
        neutros = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] == 0].count().values[0]
        positivos = tiktok_sentiment_posts[tiktok_sentiment_posts["sentimiento"] > 0].count().values[0]

        # Crear la gráfica de pastel
        labels = ["Negativos", "Neutros", "Positivos"]
        values = [negativos, neutros, positivos]

        #fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        # Crear la figura de pastel con formato personalizado
        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Establecer el radio del hoyo en 0.5 para crear un hoyo en el medio
        pull=[0.1, 0.1, 0.1],  # Separar las porciones del pastel
        textinfo='label+percent',  # Mostrar etiquetas y porcentajes en la leyenda
        marker=dict(colors=['#1f77b4', '#be00c7', '#2ca02c']),  # Colores personalizados
        direction='counterclockwise',  # Dirección de rotación del pastel
        sort=False  # Desactivar la clasificación automática de las porciones
        )])

        # Actualizar el diseño de la figura
        fig.update_layout(
        title='Análisis de Polaridad en los comentarios',  # Establecer el título
        legend=dict(orientation='h', yanchor='bottom', y=-0.2),  # Colocar la leyenda debajo
        template='new_template'  # Utilizar el tema editado arriba
        )

        return fig


@app.callback(
        Output("graph_words", "figure"),
        Input("opcion-selector", "value"))

def update_graph(selector):
    if selector == 'Twitter':
        ####################################
        # Crear la gráfica de barras horizontales
        # Ordenar el DataFrame por frecuencia de forma descendente

        fig = go.Figure(go.Bar(
            x=top_words['count'],  # Valores en el eje x (frecuencias)
            y=top_words['words'],  # Categorías en el eje y (palabras)
            orientation='h'  # Orientación horizontal
        ))

        # Configurar el diseño de la gráfica
        fig.update_layout(
            title='Frecuencia de Palabras en los posts',
            xaxis_title='Frecuencia',
            xaxis=dict(title_standoff=10),
        )
        return fig

    elif selector == 'TikTok':
        fig = go.Figure(go.Bar(
            x=tiktok_words_posts['count'],  # Valores en el eje x (frecuencias)
            y=tiktok_words_posts['words'],  # Categorías en el eje y (palabras)
            orientation='h'  # Orientación horizontal
        ))

        # Configurar el diseño de la gráfica
        fig.update_layout(
            title='Frecuencia de Palabras en los posts',
            xaxis_title='Frecuencia',
            xaxis=dict(title_standoff=10),
        )
        return fig


@app.callback(
        Output("graph_words_coments", "figure"),
        Input("opcion-selector", "value"))

def update_graph(selector):
    if selector == 'Twitter':
        ####################################
        # Crear la gráfica de barras horizontales
        # Ordenar el DataFrame por frecuencia de forma descendente

        fig = go.Figure(go.Bar(
            x=top_words_coments_twitter['count'],  # Valores en el eje x (frecuencias)
            y=top_words_coments_twitter['words'],  # Categorías en el eje y (palabras)
            orientation='h'  # Orientación horizontal
        ))

        # Configurar el diseño de la gráfica
        fig.update_layout(
            title='Frecuencia de Palabras en los comentarios',
            xaxis_title='Frecuencia',
            xaxis=dict(title_standoff=10),
        )
        return fig

    elif selector == 'TikTok':
        fig = go.Figure(go.Bar(
            x=tiktok_words_coments['count'],  # Categorías en el eje y (palabras)
            y=tiktok_words_coments['words'],
            orientation='h'  # Orientación horizontal
        ))

        # Configurar el diseño de la gráfica
        fig.update_layout(
            title='Frecuencia de Palabras en los posts',
            xaxis_title='Frecuencia',
            xaxis=dict(title_standoff=10),
        )
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
