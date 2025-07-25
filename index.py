mport yfinance as yf
import pandas as pd

# Fetch historical stock data for Tesla
stock_data = yf.download('TSLA', start='2016-10-01', end='2024-10-01')

# Display the first few rows of the dataset
stock_data.head()
