import pandas as pd
import geopandas as gpd
import folium
from branca.colormap import linear

archivo = gpd.read_file("/home/cygnus/Documentos/mapas/secciones_2024.gpkg/secciones_2024.gpkg")
tampico = archivo[archivo['NOMBRE_MUNICIPIO'] == 'TAMPICO']
df_21 = pd.read_csv("ayuntamiento_2021.csv")
df_21['SECCION'] = df_21['CASILLA'].str.split(' ', expand=True)[0]



def calcular_switchers(row):
    if row['Frente amplio'] > row['Juntos haremos historia']:
        if row['Frente amplio'] - row['Juntos haremos historia'] < row['Porcentaje']:
            return 2
        elif row['Frente amplio'] - row['Juntos haremos historia'] > row['Porcentaje']:
            return 3
    elif row['Frente amplio'] < row['Juntos haremos historia']:
        if row['Juntos haremos historia'] - row['Frente amplio'] < row['Porcentaje']:
            return 2
        elif row['Juntos haremos historia'] - row['Frente amplio'] > row['Porcentaje']:
            return 1
    else:
        return 1


df_agrupado = df_21.groupby('SECCION').sum()
df_agrupado = df_agrupado.reset_index()
df_agrupado['SECCION'] = df_agrupado['SECCION'].astype(int)
df_agrupado['Frente amplio'] = df_agrupado['PAN'] + df_agrupado['PRI'] + df_agrupado['PRD'] 
df_agrupado['Juntos haremos historia'] = df_agrupado['MORENA'] + df_agrupado['PT-MORENA'] + df_agrupado['PT'] + df_agrupado['PVEM'] + df_agrupado['PES'] + df_agrupado['RSP'] + df_agrupado['FXM']
df_agrupado['Participación'] = df_agrupado['PAN'] + df_agrupado['PRI'] + df_agrupado['PRD'] + df_agrupado['MORENA'] + df_agrupado['PT-MORENA'] + df_agrupado['PT'] + df_agrupado['PVEM'] + df_agrupado['PES'] + df_agrupado['RSP'] + df_agrupado['FXM'] + df_agrupado['VOTOS\n NULOS']
df_agrupado['Porcentaje'] = df_agrupado['Participación'] * 0.1
df_agrupado['switchers'] = df_agrupado.apply(calcular_switchers, axis=1)


Tampico = tampico.merge(df_agrupado, how='left', on='SECCION')
Tampico = Tampico.fillna(0)

m = folium.Map([22.266475239517746, -97.86747689702946], zoom_start=13)

# Crea la choropleth con la lista de colores personalizada
folium.Choropleth(
    geo_data=Tampico,
    data=Tampico,
    columns=["SECCION", "switchers"],
    key_on='feature.properties.SECCION',
    fill_opacity=0.7,
    line_opacity=0.2,
    name="Switchers 2021",
    legend_name="Switchers",
    highlight=True,
    nan_fill_color='gray',
    nan_fill_opacity=0.4,
    show=False,
    fill_color='Paired',
).add_to(m)

folium.Choropleth(
    geo_data=Tampico,
    data=Tampico,
    columns=['SECCION', 'LISTA_NOMINAL'],  # Columna de identificación y de valores para la escala
    key_on='feature.properties.SECCION',  # Clave para realizar la unión entre el GeoDataFrame y la capa GeoJSON
    fill_color='YlGnBu',  # Esquema de colores
    fill_opacity=0.7,
    line_opacity=0.2,
    name='Lista Nominal',  # Nombre de la leyenda
).add_to(m)


def tooltip_content(row):
    return f"""
    <h3>Resultados Electorales 2021</h3>
    <strong>Sección:</strong> {row['SECCION']}<br>
    <strong>MC:</strong> {row['MC']}<br>
    <strong>Frente Amplio:</strong> {row['Frente amplio']}<br>
    <strong>Juntos haremos historia:</strong> {row['Juntos haremos historia']}<br>
    """

# Creación de marcadores con tooltip
for idx, row in Tampico.iterrows():
    lat = row.geometry.centroid.y
    lon = row.geometry.centroid.x
    tooltip = folium.Html(tooltip_content(row), script=True)
    popup = folium.Popup(tooltip, max_width=2650)
    folium.Marker(location=[lat, lon], popup=popup, icon=folium.Icon(color='blue', icon='info-sign')).add_to(m)


folium.LayerControl(collapsed=False).add_to(m)




m.save("switchers.html")