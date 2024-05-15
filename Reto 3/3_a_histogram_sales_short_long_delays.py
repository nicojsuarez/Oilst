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
delivered = delivered[delivered['delay_status'] != 'on_time']

# Especifica el tamaño de la figura
plt.figure(figsize = (15,6))

# Genera el histograma
sns.histplot(
    data=delivered,
    x="total_sales",
    hue="delay_status",
    bins=100
    ).set(
        title='Histograma de frecuencias de la diferencia de la variable total_sales \n por tipo de tipo de orden'
        )

plt.savefig('3_a_histogram_sales_short_long_delays.png')