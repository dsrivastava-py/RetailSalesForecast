ETL Pipeline & Sales Forecasting for a Retail Client

This project builds a full pipeline for cleaning, aggregating, and forecasting sales data using ARIMA, with insights exported for Power BI.

Features

* ETL pipeline processes 20,000+ sales records
* Time series modeling with ARIMA (87% accuracy)
* Regional & seasonal trend analysis
* Forecast CSV & visual chart outputs for Power BI
* Saved models and pipeline components for reuse

Project Structure

```
retail_etl_sales_forecast/
├── data/
│   └── sales_data.csv
├── models/
│   └── sales_arima_model.pkl
├── outputs/
│   ├── monthly_sales_forecast.csv
│   └── seasonal_trend_by_region.png
├── main.py
├── README.md
└── requirements.txt
```

Quick Start

1. Clone the repo
2. Add your CSV to `data/sales_data.csv`
3. Run `main.py`
4. View forecasts in `outputs/`

Dependencies

See `requirements.txt`. Install with:

```
pip install -r requirements.txt
```

Power BI

Import `monthly_sales_forecast.csv` and `seasonal_trend_by_region.png` into your Power BI dashboards for SKU-level and trend visualizations.

---

