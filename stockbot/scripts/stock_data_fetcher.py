import requests
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
print(API_KEY)
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol, interval="1min", output_size="compact"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": API_KEY,
        "outputsize": output_size
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print(f"HTTP Error: {response.status_code}")
        print(response.text)
        return None

    data = response.json()

    if f"Time Series ({interval})" in data:
        time_series = data[f"Time Series ({interval})"]
        df = pd.DataFrame.from_dict(time_series, orient="index")
        df.rename(columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume"
        }, inplace=True)
        df.index = pd.to_datetime(df.index)
        return df
    else:
        print("Error:", data.get("Error Message", "Unable to fetch data."))
        return None
    
if __name__ == "__main__":
    symbol = "AAPL"
    interval = "1min"
    output_size = "compact"

    print(f"Fetching data for {symbol} with interval {interval} and output size {output_size}...")

    stock_data = fetch_stock_data(symbol, interval, output_size)

    if stock_data is not None:
        print(stock_data.head())
    else:
        print("Failed to fetch stock data.")