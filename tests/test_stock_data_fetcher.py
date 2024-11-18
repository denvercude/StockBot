import os
from stockbot.scripts.stock_data_fetcher import fetch_stock_data

def test_fetch_stock_data():
    """
    Test the fetch_stock_data function to ensure it retrieves valid data.
    """
    # Ensure the API key is set correctly
    assert os.getenv("ALPHA_VANTAGE_API_KEY") is not None, "API key is not set in the environment."
    
    # Fetch data for a known stock symbol
    data = fetch_stock_data("AAPL", interval="1min", output_size="compact")
    
    # Check if the data is a non-empty DataFrame
    assert data is not None, "fetch_stock_data returned None."
    assert not data.empty, "fetch_stock_data returned an empty DataFrame."
    assert "open" in data.columns, "'open' column missing in fetched data."
    assert "close" in data.columns, "'close' column missing in fetched data."
    assert "volume" in data.columns, "'volume' column missing in fetched data."

    print("Test passed: fetch_stock_data works as expected.")

if __name__ == "__main__":
    test_fetch_stock_data()