#Explore your chosen retail time series using the following functions:

#plot_series(), seasonal_decompose(), lag_plot(), plot_acf()

#Can you spot any seasonality, cyclicity and trend? What do you learn about the series?

from sktime.utils.plotting import plot_series
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Carregar dados
retail = pd.read_csv("./data/aus_retail.csv")

# Selecionar série aleatória conforme exercício
np.random.seed(12345678)
random_series_id = np.random.choice(retail['Series ID'].unique(), 1)[0]
myseries = retail.query(f"`Series ID` == '{random_series_id}'")

# Preparar dados temporais
myseries['Month'] = pd.to_datetime(myseries['Month'])
myseries = myseries.set_index('Month').sort_index()
ts_data = myseries['Turnover']

print(f"Série selecionada: {random_series_id}")
print(f"Indústria: {myseries['Industry'].iloc[0]}")

# Criar a figura e os subplots desde o início
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. plot_series() - Primeiro subplot (superior esquerdo)
plot_series(ts_data, ax=axes[0, 0]) 
axes[0, 0].set_title('Série Temporal')

# 2. seasonal_decompose() 
decomposed = seasonal_decompose(ts_data, model='additive', period=12)

# Tendência - Segundo subplot (superior direito)
plot_series(decomposed.trend.dropna(), ax=axes[0, 1])
axes[0, 1].set_title('Tendência')

# Sazonalidade - Terceiro subplot (inferior esquerdo)
plot_series(decomposed.seasonal, ax=axes[1, 0])
axes[1, 0].set_title('Sazonalidade')

# 3. plot_acf() - Quarto subplot (inferior direito)
plot_acf(ts_data.dropna(), lags=24, ax=axes[1, 1])
axes[1, 1].set_title('Autocorrelação')

plt.tight_layout()
plt.show()

# Análise dos padrões
print("\nPadrões identificados:")
print(f"- Sazonalidade: {'Sim' if decomposed.seasonal.std() > 0.1 else 'Não'}")
print(f"- Tendência: {'Crescente' if decomposed.trend.dropna().iloc[-1] > decomposed.trend.dropna().iloc[0] else 'Decrescente'}")
print(f"- Ciclicidade: Verificar ACF para ciclos além de 12 meses")