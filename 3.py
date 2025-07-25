from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

df_tute = pd.read_csv("./data/tute1.csv")

df_tute['ds'] = pd.to_datetime(df_tute['Quarter'])
df_tute = df_tute.drop(['Quarter'], axis=1)


tute_indexed = df_tute.set_index("ds")

print(tute_indexed.head())

plot_series(tute_indexed["Sales"])
plot_series(tute_indexed["AdBudget"])
plot_series(tute_indexed["GDP"])
plt.show()