# Without re-indexing, the index still references the number of the line in the original dataframe, starting from entry 19877

# The changes in stock price do look like white noise, because they can't be exactly predicted and are affected
# by a number of factors to which we do not have access

from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import lag_plot
import pandas as pd
import numpy as np

# Carregar dados
stock = pd.read_csv("./data/gafa_stock.csv")
stock["ds"] = pd.to_datetime(stock["ds"])

dgoog =  stock.query('unique_id == "GOOG_Close" & ds >= "2018"')
dgoog['trading_day'] = np.arange(1, len(dgoog) + 1)
dgoog['diff'] = dgoog['y'].diff()

dgoog_diff = dgoog[['ds', 'diff']].set_index('ds')


plot_series(dgoog.set_index('ds')['diff'], labels=['Difference'])
plt.title('Google Stock Price Differences')
plt.show()

plot_acf(dgoog_diff.dropna(), lags=24)
plt.show()
