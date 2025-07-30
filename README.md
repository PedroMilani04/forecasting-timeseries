# Time Series Data Handling and Visualization with `sktime` and `statsmodels`

This repository contains solutions and practical exercises for **Topic 2.10: Exercises** from the textbook "[Forecasting: Principles and Practice, the Pythonic Way](https://otexts.com/fpppy/nbs/02-graphics.html#sec-graphics-exercises)". It implements a **time series analysis pipeline** focusing on the crucial initial steps: data preparation and graphical exploration using key Python libraries.

---

## Project Overview

The primary objective of these challenges is to build foundational skills in time series analysis by loading, preparing, decomposing, and visualizing time series data. This practical approach helps in understanding the inherent patterns before moving into forecasting models.

1.  **Data Loading & Preparation**
    The `aus_retail.csv` dataset is loaded using `pandas`. A specific time series is randomly selected and prepared by converting the 'Month' column to `datetime` objects and setting it as the DataFrame's index for proper time series handling.

2.  **Time Series Visualization (`sktime.utils.plotting.plot_series`)**
    The selected time series is plotted to enable visual inspection of its overall behavior. This step is vital for identifying underlying trends, seasonal fluctuations, and potential anomalous observations.

3.  **Seasonal Decomposition (`statsmodels.tsa.seasonal.seasonal_decompose`)**
    The time series is decomposed into its fundamental components: trend, seasonal, and residual (irregular) parts. This decomposition helps to discern and quantify the additive or multiplicative nature of recurring patterns and long-term movements.

4.  **Autocorrelation Analysis (`statsmodels.graphics.tsaplots.plot_acf`)**
    The Autocorrelation Function (ACF) plot is generated to measure the linear dependence of an observation on observations at various previous time steps (lags). This plot is instrumental in identifying the presence of white noise, trends, seasonal patterns, and in assessing the stationarity of the series. The confidence interval (shaded area) helps determine the statistical significance of these correlations.

---

## Key Learning Outcomes & Features

1.  **Foundational Time Series Data Handling**
    Practical application of `pandas` for time series specific operations, including data loading, `datetime` conversion, and proper indexing for time-based analysis. Produces console output for selected series details.

2.  **Exploratory Data Analysis with Visuals**
    Mastery of plotting techniques with `sktime` and `matplotlib` to visually interpret time series behavior, uncovering insights into trends, seasonality, and overall structure via interactive plots of the raw series, its trend, and seasonality.

3.  **Understanding Time Series Components**
    Ability to apply and interpret seasonal decomposition, effectively separating a series into its core trend, seasonal, and residual elements, which is a prerequisite for many forecasting models.

4.  **Autocorrelation Interpretation**
    Proficiency in generating and interpreting ACF plots, using the confidence interval to identify statistically significant autocorrelations. This provides diagnostic insights into the series' stationarity and dependency structure, leading to console output summarizing identified patterns (seasonality, trend, cyclicity).

---

## Libraries Used

-   `pandas` – for robust data manipulation and time series handling
-   `numpy` – for numerical operations
-   `matplotlib` – for extensive data visualization
-   `sktime` – for high-level time series plotting utilities
-   `statsmodels` – for time series decomposition and autocorrelation analysis

---
