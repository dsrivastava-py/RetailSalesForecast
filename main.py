# File: retail_etl_sales_forecast/main.py

import pandas as pd
import numpy as np
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import joblib

# ----------------------------
# 1. ETL: Load and Clean Sales Data
# ----------------------------
data_path = "data/sales_data.csv"
data = pd.read_csv(data_path, parse_dates=['date'])
data.columns = data.columns.str.strip()

# Ensure clean data types
data = data.dropna(subset=['date', 'sales', 'region', 'sku'])
data = data[data['sales'] >= 0]

# ----------------------------
# 2. Aggregate Monthly Sales
# ----------------------------
data['month'] = data['date'].dt.to_period('M').dt.to_timestamp()
monthly_sales = data.groupby('month')['sales'].sum().reset_index()

# ----------------------------
# 3. Time Series Forecasting with ARIMA
# ----------------------------
train = monthly_sales.set_index('month')['sales']

# ARIMA with seasonal component (SARIMAX)
model = SARIMAX(train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit(disp=False)

# Forecast next 6 months
forecast_steps = 6
forecast = model_fit.forecast(steps=forecast_steps)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model_fit, "models/sales_arima_model.pkl")

# ----------------------------
# 4. Trend Analysis (Seasonal/Regional)
# ----------------------------
# Monthly seasonality by region
regional_trend = data.groupby([data['date'].dt.month, 'region'])['sales'].sum().unstack().fillna(0)

plt.figure(figsize=(10, 6))
regional_trend.plot()
plt.title("Seasonal Trend by Region")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(title="Region")
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/seasonal_trend_by_region.png")

# ----------------------------
# 5. Save Forecast Output
# ----------------------------
forecast_index = pd.date_range(start=monthly_sales['month'].max() + pd.offsets.MonthBegin(1), periods=forecast_steps, freq='MS')
forecast_df = pd.DataFrame({
    'month': forecast_index,
    'forecasted_sales': forecast.values
})
forecast_df.to_csv("outputs/monthly_sales_forecast.csv", index=False)

print("Forecast and analysis saved to outputs/")
