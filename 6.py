from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

aus_arrivals = pd.read_csv("./data/aus_arrivals.csv")


aus_arrivals["Quarter"] = pd.to_datetime(aus_arrivals["Quarter"])

aus_arrivals = aus_arrivals.set_index("Quarter")
print(aus_arrivals)

japan = aus_arrivals[aus_arrivals['Origin'] == 'Japan']
nz = aus_arrivals[aus_arrivals['Origin'] == 'NZ']
uk = aus_arrivals[aus_arrivals['Origin'] == 'UK']
us = aus_arrivals[aus_arrivals['Origin'] == 'US']

plt.figure(figsize=(12, 6))
plt.plot(japan.index, japan['Arrivals'], label='Japan', color='red')
plt.plot(nz.index, nz['Arrivals'], label='New Zealand', color='blue')
plt.plot(uk.index, uk['Arrivals'], label='UK', color='green')
plt.plot(us.index, us['Arrivals'], label='US', color='purple')

plt.title('Tourist Arrivals by Country of Origin')
plt.xlabel('Quarter')
plt.ylabel('Arrivals')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
