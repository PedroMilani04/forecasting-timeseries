from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt # É uma boa prática importar o matplotlib para exibir o plot

import pandas as pd;

df_prod = pd.read_csv("./data/aus_production.csv")
df_gafa = pd.read_csv("./data/gafa_stock.csv")
df_pelt = pd.read_csv("./data/pelt.csv")
df_elec = pd.read_csv("./data/vic_elec.csv")

bricks = df_prod[["ds", "Bricks"]]
lynx = df_pelt[df_pelt["unique_id"] == "lynx"][["ds", "y"]]
goog_close = df_gafa[df_gafa["unique_id"] == "GOOG_Close"][["ds", "y"]]
demand = df_elec[df_elec["unique_id"] == "Demand"][["ds", "y"]]

bricks["ds"] = pd.to_datetime(bricks["ds"])
lynx["ds"] = pd.to_datetime(lynx["ds"])
goog_close["ds"] = pd.to_datetime(goog_close["ds"])
demand["ds"] = pd.to_datetime(demand["ds"])

bricks_interval = bricks["ds"].diff()
lynx_interval = lynx["ds"].diff()
goog_close_interval = goog_close["ds"].diff()
demand_interval = demand["ds"].diff()

print("Bricks info:")
print(bricks.info())
print("Bricks interval:")
print(bricks_interval) # trimestral
print("\nLynx info:")
print(lynx.info()) 
print("Lynx interval:")
print(lynx_interval) # anual
print("\nGoogle Close info:")
print(goog_close.info())
print("Google Close interval:") 
print(goog_close_interval) # 1-3 dias
print("\nDemand info:")
print(demand.info())
print("Demand interval:")
print(demand_interval) # 30 minutos


bricks_indexed = bricks.set_index("ds")
lynx_indexed = lynx.set_index("ds")
goog_close_indexed = goog_close.set_index("ds")
demand_indexed = demand.set_index("ds")

plot_series(bricks_indexed)
plt.title('Brick Production Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Bricks')
#plt.show()

plot_series(lynx_indexed)
plt.title('Lynx')
#plt.show()

plot_series(goog_close_indexed)
plt.title('Google Stock Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
#plt.show()

plot_series(demand_indexed)
plt.title('Electricity Demand')
plt.xlabel('Date')
plt.ylabel('Demand (MW)')
#plt.show()

print("Maior Close para Google: ")
print(df_gafa.query("unique_id == 'GOOG_Close'")['y'].max())

print("Maior Close para Facebook: ")
print(df_gafa.query("unique_id == 'FB_Close'")['y'].max())

print("Maior Close para Amazon: ")
print(df_gafa.query("unique_id == 'AMZN_Close'")['y'].max())

print("Maior Close para Apple: ")
print(df_gafa.query("unique_id == 'AAPL_Close'")['y'].max())