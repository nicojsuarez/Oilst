import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

cols_corr = [
    'total_sales',
    'total_products',
    'delta_days',
    'distance_distribution_center'
    ]
matrix_corr = delivered.filter(cols_corr).corr()   

sns.heatmap(
    matrix_corr,
    cmap="coolwarm",
    annot=True).set(
        title='Fig. 9 Matriz de correlación de las órdenes'
        )
plt.savefig('3_b_correlation_matrix_complete_orders.png')