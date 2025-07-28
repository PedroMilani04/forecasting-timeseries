#Use the following graphics functions: plot_series(), seasonal_decompose(), lag_plot(), plot_acf() and explore features from the following time series: 
# "Total Private" Employed from us_employment, Bricks from aus_production, Hare from pelt, "H02" Cost from PBS, and Barrels from us_gasoline.

#Can you spot any seasonality, cyclicity and trend?
#What do you learn about the series?
#What can you say about the seasonal patterns?
#Can you identify any unusual years?

from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import lag_plot
import pandas as pd

# Carregar dados
df_prod = pd.read_csv("./data/aus_production.csv")
df_employed = pd.read_csv("./data/us_employment.csv")
df_pelt = pd.read_csv("./data/pelt.csv")
df_pbs = pd.read_csv("./data/pbs.csv")
df_gasoline = pd.read_csv("./data/us_gasoline.csv")

# Preparar dados
bricks = df_prod[["ds", "Bricks"]].copy()
hare = df_pelt[df_pelt["unique_id"] == "hare"][["ds", "y"]].copy()
employed = df_employed[df_employed["unique_id"] == "Total Private"][["ds", "y"]].copy()
H02cost = df_pbs[df_pbs["ATC2"] == "H02"][["Month", "Cost"]].copy()
barrels = df_gasoline[df_gasoline["unique_id"] == "us_gasoline"][["ds", "y"]].copy()

bricks["ds"] = pd.to_datetime(bricks["ds"])
hare["ds"] = pd.to_datetime(hare["ds"])
employed["ds"] = pd.to_datetime(employed["ds"])
H02cost["Month"] = pd.to_datetime(H02cost["Month"])
barrels["ds"] = pd.to_datetime(barrels["ds"])

# Definir índices e ordenar
bricks = bricks.set_index("ds").sort_index()
hare = hare.set_index("ds").sort_index()
employed = employed.set_index("ds").sort_index()
H02cost = H02cost.set_index("Month").sort_index()
barrels = barrels.set_index("ds").sort_index()

# 1. PLOT DAS SÉRIES ORIGINAIS
plt.figure(figsize=(15, 12))

plt.subplot(5,1,1)
plt.plot(bricks.index, bricks['Bricks'])
plt.title('Bricks Production')
plt.grid(True)

plt.subplot(5,1,2)
plt.plot(hare.index, hare['y'])
plt.title('Hare Population')
plt.grid(True)

plt.subplot(5,1,3)
plt.plot(employed.index, employed['y'])
plt.title('Total Private Employment')
plt.grid(True)

plt.subplot(5,1,4)
plt.plot(barrels.index, barrels['y'])
plt.title('US Gasoline Barrels')
plt.grid(True)

plt.subplot(5,1,5)
plt.plot(H02cost.index, H02cost['Cost'])
plt.title('H02 Cost')
plt.grid(True)

plt.tight_layout()
plt.show()

# 2. FUNÇÃO PARA DECOMPOSIÇÃO E PLOTS
def plot_decomposition(series, title, period=12):
    """Plota decomposição sazonal completa para uma série"""
    # Limpar dados
    series_clean = series.dropna()
    
    # Decomposição sazonal
    decomposed = seasonal_decompose(series_clean, model='additive', period=period)
    
    # Plot da decomposição
    fig, axes = plt.subplots(4, 1, figsize=(15, 10))
    fig.suptitle(f'Seasonal Decomposition - {title}', fontsize=16)
    
    # Série original
    axes[0].plot(series_clean.index, series_clean.iloc[:, 0])
    axes[0].set_title('Original Series')
    axes[0].grid(True)
    
    # Tendência
    trend_clean = decomposed.trend.dropna()
    axes[1].plot(trend_clean.index, trend_clean)
    axes[1].set_title('Trend')
    axes[1].grid(True)
    
    # Sazonalidade
    axes[2].plot(decomposed.seasonal.index, decomposed.seasonal)
    axes[2].set_title('Seasonal')
    axes[2].grid(True)
    
    # Resíduos
    resid_clean = decomposed.resid.dropna()
    axes[3].plot(resid_clean.index, resid_clean)
    axes[3].set_title('Residual')
    axes[3].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return decomposed

# 3. DECOMPOSIÇÃO PARA CADA SÉRIE

print("=== BRICKS PRODUCTION ===")
decomp_bricks = plot_decomposition(bricks, "Bricks Production", period=12)

print("\n=== HARE POPULATION ===")
decomp_hare = plot_decomposition(hare, "Hare Population", period=12)

print("\n=== TOTAL PRIVATE EMPLOYMENT ===")
decomp_employed = plot_decomposition(employed, "Total Private Employment", period=12)

print("\n=== US GASOLINE BARRELS ===")
decomp_barrels = plot_decomposition(barrels, "US Gasoline Barrels", period=12)

print("\n=== H02 COST ===")
decomp_H02 = plot_decomposition(H02cost, "H02 Cost", period=12)

# 4. AUTOCORRELATION PLOTS
def plot_acf_analysis(series, title, lags=24):
    """Plota ACF para análise de correlação"""
    series_clean = series.dropna()
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle(f'ACF Analysis - {title}', fontsize=14)
    
    # Série original
    axes[0].plot(series_clean.index, series_clean.iloc[:, 0])
    axes[0].set_title('Original Series')
    axes[0].grid(True)
    
    # ACF
    plot_acf(series_clean.iloc[:, 0], lags=lags, ax=axes[1])
    axes[1].set_title('Autocorrelation Function')
    
    plt.tight_layout()
    plt.show()

print("\n=== AUTOCORRELATION ANALYSIS ===")

# ACF para todas as séries
plot_acf_analysis(bricks, "Bricks Production")
plot_acf_analysis(hare, "Hare Population")
plot_acf_analysis(employed, "Total Private Employment")
plot_acf_analysis(barrels, "US Gasoline Barrels")
plot_acf_analysis(H02cost, "H02 Cost")


