import requests
import pandas as pd
import logging
from transform import transform_crypto_data

logging.basicConfig(level=logging.INFO)

def fetch_crypto_data(limit=20):
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency" : "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)
    df = df[df["symbol"].notnull()]
    df.fillna({"current_price":0, "market_cap":0, "total_volume":0}, inplace=True)
    
    logging.info("Fetching %d rows", len(df))

    df = df[
        [
            "symbol",
            "current_price",
            "market_cap",
            "total_volume",
        ]
    ]

    df["current_price"] = df["current_price"].round(2)
    df["market_cap"] = (df["market_cap"] / 1e9).round(2)
    df["total_volume"] = (df["total_volume"] / 1e9).round(2)
    
    return df

if __name__ == "__main__":
    df = fetch_crypto_data()
    df = transform_crypto_data(df)

    print(df.head())
    print(df.dtypes)