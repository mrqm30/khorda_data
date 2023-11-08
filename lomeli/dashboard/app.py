import dash
import numpy as np
import pandas as pd
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import plotly.io as pio

pio.templates['new_template'] = go.layout.Template()
pio.templates['new_template']['layout']['font'] = {'family': 'verdana', 'size': 16, 'color': 'black'}
pio.templates['new_template']['layout']['paper_bgcolor'] = '#f3f4f6'
pio.templates['new_template']['layout']['plot_bgcolor'] = '#f3f4f6'
pio.templates['new_template']['layout']['xaxis'] = {'title_standoff': 10, 'linecolor': '#f3f4f6', 'mirror': True, 'gridcolor': '#EEEEEE'}
pio.templates['new_template']['layout']['yaxis'] = {'title_standoff': 10, 'linecolor': '#f3f4f6', 'mirror': True, 'gridcolor': '#EEEEEE'}
pio.templates['new_template']['layout']['legend_bgcolor'] = 'rgb(117, 112, 179)'
pio.templates['new_template']['layout']['height'] = 550
pio.templates['new_template']['layout']['width'] = 600
pio.templates['new_template']['layout']['autosize'] = False

pio.templates.default = 'new_template'
##DATOS PARA POLARIDAD 
polaridad = pd.read_csv("/home/milton/Documentos/khorda_data/lomeli/dashboard/data/polaridad.csv")

fig = go.Figure()
fig.add_trace(go.Histogram(x=polaridad.polaridad, histnorm='probability', marker_color='blue'))
# Personalizar el diseño y agregar elementos visuales
fig.update_layout(
    title_text="Distribución de Polaridad",
    xaxis_title="Polaridad",
    yaxis_title="Frecuencia",
    xaxis=dict(showline=True, showgrid=False),
    yaxis=dict(showline=True, showgrid=False),
    bargap=0.0,  # Espaciado entre barras
    bargroupgap=0.0,  # Espaciado entre grupos de barras
    showlegend=False,  # No mostrar leyenda
    template="new_template"
)

mediana = np.median(polaridad)

# Clasificar las polaridades en negativas, neutras y positivas
negativas = polaridad[(polaridad['polaridad'] > 0.1) & (polaridad['polaridad'] < 0.4)]
neutras = polaridad[(polaridad['polaridad'] > 0.4) & (polaridad['polaridad'] <= 0.5)]
positivas = polaridad[(polaridad['polaridad'] > 0.5)]


# Contar cuántos elementos hay en cada categoría
num_negativas = len(negativas)
num_neutras = len(neutras)
num_positivas = len(positivas)

# Crear la gráfica de pastel
labels = ['Negativas', 'Neutras', 'Positivas']
sizes = [num_negativas, num_neutras, num_positivas]
colors = ['#00D', '#7B68EE', '#ADFF2F']

fig_pie = go.Figure(data=[go.Pie(labels=labels, hole=0.5,
                            values=sizes)])
fig_pie.update_traces(
    hoverinfo='label+percent',
    textinfo='value+percent',
    textfont_size=20,
    marker=dict(
        colors=colors,
        line=dict(color='cyan', width=2)))
fig_pie.update_layout(
    title="Distribución de Polaridad",
    font=dict(family="Arial", size=20, color="black"),
    template="new_template",
    margin=dict(l=0, r=0, b=0, t=50),
    legend=dict(
        orientation='h',
        x=0.2,
        y=-0.2
    )
)



emociones = pd.read_csv("/home/milton/Documentos/khorda_data/lomeli/dashboard/data/emocion.csv")

emocion = emociones[emociones['emocion'] != 'neutral']

conteo_emociones = emocion['emocion'].value_counts().reset_index()
conteo_emociones.columns = ['Emoción', 'Cantidad']

# Crear un treemap con Plotly Express
fig_treemap = px.treemap(conteo_emociones, path=['Emoción'], values='Cantidad')
# Personaliza el diseño
fig_treemap.update_layout(
    title='Distribución de Emociones',  # Cambia el título según tu preferencia
    margin=dict(l=0, r=0, b=0, t=50),  # Ajusta los márgenes
    font=dict(family="Arial", size=16, color="black"),  # Personaliza la fuente
    paper_bgcolor='#f3f4f6',  # Establece el color de fondo
    treemapcolorway=['blue', 'green', 'red', 'orange', 'purple'],  # Colores personalizados
    showlegend=False ,
    template = "new_template"
)

# Personaliza el treemap
fig_treemap.update_traces(
    textinfo='label+percent entry',  # Muestra etiquetas y porcentaje
    branchvalues="total"  # Rama con valores totales
)

# Ajusta el tamaño de la fuente del título y las etiquetas
fig_treemap.update_layout(title_font_size=22)
fig_treemap.update_traces(textfont_size=22)


# Crear radar
social = pd.read_csv("/home/milton/Documentos/khorda_data/lomeli/dashboard/data/social.csv")
social_group = social.groupby('red_social').sum().reset_index()
fig_radar = go.Figure()
for col in ['views_reactions_log']:#'comentarios','repost','likes',
  fig_radar.add_trace(go.Barpolar(#Scatterpolar
      r=social_group[col],
      theta=social_group.red_social,
      #fill='toself',
      name = col,
      hoverinfo='text',
      hovertext=[f"RS : {elem.red_social}; Views : {int(elem[col])}" for _, elem in social_group.iterrows()],
      opacity=0.5
      ))
fig_radar.update_layout(
  polar=dict(
  bgcolor='rgba(0,0,0,0)', 
  radialaxis=dict(
      visible=False
    ),
    angularaxis=dict(
    direction='counterclockwise',  # Para cambiar la dirección del eje theta
        )),
  showlegend=False,
  font_size=16,
  legend_font_size=12,
  height=500,
  width=500,
  template='new_template'
)


fig_radar_2 = go.Figure()
for col in ['comentarios','repost','likes','views_reactions_log']:
  fig_radar_2.add_trace(go.Barpolar(
      r=social_group[col],
      theta=social_group.red_social,
      name = col,
      hoverinfo='text',
      hovertext=[f"RS : {elem.red_social}; Views : {int(elem[col])}" for _, elem in social_group.iterrows()],
      opacity=0.5
      ))
fig_radar_2.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=False
    )),
  showlegend=True,
  font_size=16,
  legend_font_size=16,
  height=500,
  width=500,
  template="new_template",
  legend=dict(
        x=0.3,  # Centrado horizontalmente
        y=-1  # Colocado en la parte superior
    )
)
########################################################################
topics = pd.read_csv("/home/milton/Documentos/khorda_data/lomeli/dashboard/data/topicos.csv")

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
                        social_button(app, 'facebook.png', 'Facebook', 'button-3'),
                        html.Br(),
                        social_button(app, 'instagram.png', 'Instagram', 'button-4'),
                        html.Br(),
                        html.Div(
                        className="flex items-center justify-center",
                        children=[dcc.Graph(id='social-graph', figure=fig_radar)]),
                        html.Br(),
                        html.Div(
                        className="flex items-center justify-center",
                        children=[dcc.Graph(id='social-graph_2', figure=fig_radar_2)]),
                    ]
                ),












                html.Div(
                    className="bg-gray-100 p-4 col-span-4 md:col-span-4 lg:col-span-4 xl:col-span-4 rounded-lg",
                    children=[
                        html.H1("Análisis de la Conversación Digital", className="text-center text-4xl font-bold leading-8 text-pink-600"),
                        html.Br(),
                        html.Div(
                            className="grid gap-3 grid-cols-1 lg:grid-cols-3",
                            children=[
                                dcc.Graph(figure=fig_pie),
                                html.Img(src=app.get_asset_url("coments.png")),
                                dcc.Graph(figure=fig_treemap)
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
                                    className="grid gap-1 grid-cols-1 lg:grid-cols-1",
                                    children=[
                                        html.Div(
                                            className="transform  shadow-2xl rounded-lg bg-gradient-to-r from-gray-200 to-gray-100 text-gray-900 px-4 py-2",
                                            children=[
                                                html.H1("Temas Emergentes", className="text-center text-4xl font-bold leading-8 text-pink-600")
                                            ]
                                        ),
                                        html.Div(
                                            className="transform  shadow-2xl rounded-lg bg-gradient-to-r from-gray-200 to-gray-100 text-gray-900 px-4 py-2",
                                            children=[
                                                html.Div([
                                                    dash_table.DataTable(
                                                        id='editable-table',
                                                        columns=[
                                                            {'name': col, 'id': col, 'editable': True} for col in topics.columns
                                                        ],
                                                        data=topics.to_dict('records'),
                                                        style_table={'height': '400px', 'overflowY': 'auto'},
                                                    ),
                                                    html.A("Descargar DataFrame", id="download-link", download="edited_dataframe.csv", href="", target="_blank"),
                                                ])

                                            ]
                                        ),
                                        html.Div(
                                            className="transform  shadow-2xl rounded-lg bg-gradient-to-r from-gray-200 to-gray-100 text-gray-900 px-4 py-2",
                                            style={'width': '100%', 'height': '600px'}, 
                                            children=[
                                                
                                                    html.Iframe(src=app.get_asset_url("ldavis_visualization.html"),
                                                                style={'position':"relative", 'width':"100%", 'height':"100%"})
                                                
                                            ]
                                        )
                                    
                                    ]
                                )
                            ]
                        ),
                        html.Br(),
                    ]
                )
            ]
        )
    ]
)




@app.callback(
    Output("download-link", "href"),
    Input('editable-table', 'data')
)
def update_csv(data):
    edited_df = pd.DataFrame(data)
    csv_string = edited_df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8"
    return csv_string

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
