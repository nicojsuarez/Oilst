import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import json

# Libreria de visualización
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

DATA_PATH=r"C:\Users\Administrador\Desktop\DATos\Ciclo 1\Recursos DN_COM_58"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
FILE_GEODATA = 'brasil_geodata.json'
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
FILE_REGIONS = 'brasil_regions.csv'


with open(os.path.join(DATA_PATH, FILE_GEODATA), 'r') as f:
    geojson = json.load(f)

columns_dates=[
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
    ]

oilst = pd.read_csv(
    os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA),
    parse_dates=columns_dates)

delivered = oilst.query("order_status == 'delivered'")

delivered['delay_status'] = delivered['delay_status'].replace('long_delay', 1)

a = delivered.query("delay_status == 1")
delay_by_state = a.groupby(['state_name', 'geolocation_state'], as_index=False)['delay_status'].sum()
delay_by_state = delay_by_state.sort_values(by ='delay_status', ascending=False)
delay_by_state = delay_by_state.reset_index(drop=True)
delay_by_state['delay_status'] = pd.to_numeric(delay_by_state['delay_status'], errors='coerce')

# Crear figura con el mapa de Brasil y el choropleth
fig = px.choropleth(
    data_frame=delay_by_state,
    geojson=geojson,
    featureidkey='properties.UF',
    #featureidkey='properties.ESTADO',
    locations='geolocation_state',
    # https://plotly.com/python/builtin-colorscales
    color='delay_status',
    color_continuous_scale="rainbow",
    scope='south america',
    labels={'delay_status': 'Long_delay'},
    width=800,
    height=400,
    title="# de veces que un  pedido llego tarde"
)

# Actualizar diseño de la figura
fig.update_geos(
    showcountries=False,
    showcoastlines=True,
    showland=True,
    fitbounds='locations',
    visible=True
)

fig.update_layout(
    margin=dict(l=20, r=20, t=66, b=20),
    width=800,
    height=800,
)

fig.write_html("3_e_map_long_delays_by_state.html")
fig.write_image("3_e_map_long_delays_by_state.png")