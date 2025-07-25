from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

tourism = pd.read_csv("./data/tourism.csv")

tourism['Combined'] = tourism['Purpose'] + ' - ' + tourism['Region']
tourism.drop(['Purpose', 'Region', 'State'], axis=1, inplace=True)

tourism['Quarter'] = pd.to_datetime(tourism['Quarter'])

tourism_avg = tourism.groupby('Combined')['Trips'].mean().reset_index()


print(tourism_avg)