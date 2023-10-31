#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:37:09 2023

@author: cygnus
"""

import pandas as pd

df_a = pd.read_csv("twitter_coments_lomeli.csv", usecols=["css-901oao 4","css-901oao 5", "css-901oao 7"])
df_a = df_a.fillna(" ")
df_a["texto"] = df_a["css-901oao 4"] + ' ' + df_a["css-901oao 5"] + ' ' + df_a["css-901oao 7"]

df_a = df_a.drop(columns=["css-901oao 4", "css-901oao 5", "css-901oao 7"], axis=1)

df_b = pd.read_csv("twitter_coments_lomeli_3.csv", usecols=["css-901oao 8", "css-901oao 12", "css-901oao 14"])
df_b = df_b.fillna(" ")
df_b["texto"] = df_b["css-901oao 8"] + " " + df_b["css-901oao 12"] + " " + df_b["css-901oao 14"]
df_b = df_b.drop(columns=["css-901oao 8", "css-901oao 12", "css-901oao 14"])

df_c = pd.read_csv("twitter (2).csv", usecols=["css-901oao 6"])
df_c['texto'] = df_c.fillna(' ')
df_c = df_c.drop(columns=["css-901oao 6"])
df_coments = pd.concat([df_a, df_b, df_c], axis=0)
df_coments.to_csv("coments_x.csv")