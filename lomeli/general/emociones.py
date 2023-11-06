#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 05:24:50 2023

@author: cygnus
"""

import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go

emocion_fb = pd.read_csv("/home/cygnus/Documentos/khorda_data/lomeli/facebook/coments_fb.csv", usecols=["texto", "emocion"])

emocion_x = pd.read_csv("/home/cygnus/Documentos/khorda_data/lomeli/twitter/coments_x_2.csv", encoding='latin1')

emocion_tiktok = pd.read_csv("/home/cygnus/Documentos/khorda_data/lomeli/tiktok/coments_tiktok_2.csv", usecols=["texto", "emocion"])

emocion_insta = pd.read_csv("/home/cygnus/Documentos/khorda_data/lomeli/insta/coments_insta_2.csv", usecols=["texto", "emocion"])

emocion = pd.concat([emocion_fb, emocion_x, emocion_tiktok, emocion_insta], axis=0)

emocion.to_csv("emocion.csv")

conteo_emociones = emocion['emocion'].value_counts().reset_index()
conteo_emociones.columns = ['Emoción', 'Cantidad']

# Crear un treemap con Plotly Express
fig = px.treemap(conteo_emociones, path=['Emoción'], values='Cantidad', title='Treemap de Emociones')
plot(fig)


