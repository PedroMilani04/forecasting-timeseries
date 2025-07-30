# The aus_livestock data contains the monthly total number of pigs slaughtered in Victoria, Australia, from Jul 1972 to Dec 2018. 
# Use query() to extract pig slaughters in Victoria between 1990 and 1995. 
# Use plot_series() and plot_acf() for this data. 
# How do they differ from white noise? If a longer period of data is used, what difference does it make to the ACF?

#  The more data we have, the better. The model can't make many assumptions about data behavior in a short time span. The more data you have, 
#  the better the ACF will be, because the model has much more base for assumptions, ending up with less white noise, knowing much better 
#  what is and what isn't.


from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import lag_plot
import pandas as pd

# Carregar dados
aus_livestock = pd.read_csv("./data/aus_livestock.csv")
aus_livestock["ds"] = pd.to_datetime(aus_livestock["ds"])

aus_livestock = aus_livestock.drop('unique_id', axis=1)
aus_livestock = aus_livestock.groupby('ds').sum()
aus_livestock = aus_livestock.sort_index()

aus_livestockQueried = aus_livestock.query(f"`ds` <= '1995' & `ds` >= '1990'")

print(aus_livestockQueried)

plot_series(aus_livestockQueried)

plot_acf(aus_livestockQueried.dropna(), lags=24)


plt.show()