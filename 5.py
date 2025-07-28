#Download tourism.xlsx from the book website and read in it using pd.read_excel().
#Create a dataframe using tourism.xlsx.
#Find what combination of Region and Purpose had the maximum number of overnight trips on average.
#Create a new dataframe which combines the Purposes and Regions, and just has total trips by State.

from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

tourism = pd.read_csv("./data/tourism.csv")

tourism['Combined'] = tourism['Purpose'] + ' - ' + tourism['Region']
tourism.drop(['Purpose', 'Region', 'State'], axis=1, inplace=True)

tourism['Quarter'] = pd.to_datetime(tourism['Quarter'])

tourism_avg = tourism.groupby('Combined')['Trips'].mean().reset_index()


print(tourism_avg)