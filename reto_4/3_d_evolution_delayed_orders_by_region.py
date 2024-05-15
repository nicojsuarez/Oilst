import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Libreria de visualización
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

DATA_PATH=r"C:\Users\Administrador\Desktop\DATos\Ciclo 1\Recursos DN_COM_58"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'

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


# Ventas agregadas por tipo de entrega
sales_time_delay_status = delivered.groupby(['quarter', 'delay_status'])['total_sales'].sum().reset_index()


# Agrupación de ventas por tipo de entrega normalizando para 
# el calculo de proporciones
sales_time_delay_status_tab = pd.crosstab(
    index=sales_time_delay_status['quarter'],
    columns=sales_time_delay_status['delay_status'],
    values=sales_time_delay_status['total_sales'],
    aggfunc='sum',
    normalize='index'
    )

# Se manipula la data de forma alargada
sales_time_delay_status_tab_formated = pd.melt(
    sales_time_delay_status_tab.reset_index(),
    id_vars='quarter',
    value_vars=['long_delay', 'on_time', 'short_delay']
    )

# Multiplicamos por 100 la proporcion y definimos columna en texto para plotear
sales_time_delay_status_tab_formated['value'] = sales_time_delay_status_tab_formated['value']*100.0
sales_time_delay_status_tab_formated['quarter'] = sales_time_delay_status_tab_formated['quarter'].astype('str')

fig = px.bar(
    sales_time_delay_status_tab_formated,
    x="quarter",
    y="value",
    color="delay_status",
    title="Fig. 4 Proporción de ventas de Oilst que representan las órdenes por tipo de entrega"
    )

fig.write_html("3_d_evolution_delayed_orders_by_quarter.html")


orders_time_delay_status = delivered.groupby(['year_month','delay_status']).\
    aggregate({'order_id':'count',}).\
        reset_index().\
            rename(columns={'order_id':'orders',})

# Crea una variable temporal en texto para graficar
orders_time_delay_status['period'] =  orders_time_delay_status['year_month'].astype(str)

fig = px.bar(
    orders_time_delay_status,
    x="period",
    y="orders",
    color='delay_status',
    title='Fig.2 Número de órdenes de Oilst por tipo de entrega'
)
fig.write_html("3_d_evolution_delayed_orders_by_region.html")