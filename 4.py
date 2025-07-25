from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

us = pd.read_csv("./data/us_total.csv")

new_england_states = ["Maine", "Vermont", "New Hampshire", "Massachusetts", "Connecticut", "Rhode Island"]
new_england = us[us["unique_id"].isin(new_england_states)][["ds", "y", "unique_id"]]

new_england['ds'] = pd.to_datetime(new_england['ds'], format='%Y')
new_england = new_england.groupby('ds')['y'].sum().reset_index()

print(new_england)

new_england = new_england.set_index("ds")
plot_series(new_england)
plt.show()