import requests
import pandas as pd

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency" : "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()

    df = pd.DataFrame(data)

    df = df[
        [
            "symbol",
            "current_price",
            "market_cap",
            "total_volume",
        ]
    ]
    
    return df

if __name__ == "__main__":
    crypto_df = fetch_crypto_data()
    print(crypto_df.head())