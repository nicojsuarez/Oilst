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

sns.catplot(x='delta_days',y='delay_status',hue='geolocation_state', kind='boxen', data=delivered, aspect=.6, height=10)
plt.title('Diagramas de Caja de Delta Days por Estado y Tipo de Retraso')
plt.xlabel('Delta Days')
plt.ylabel('Tipo de retrazo')
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar la figura
plt.savefig('3_c_boxplot_delta_day_by_state_and_delay_type.png')

# Mostrar el gráfico
plt.show()