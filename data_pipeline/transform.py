import pandas as pd
import logging
from datetime import datetime

def transform_crypto_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    logging.info("Transforming data with %d rows", len(df))

    # normalize column names
    df.columns = [col.lower() for col in df.columns]

    # add ingestion timestamp
    df["ingested_at"] = datetime.utcnow()

    # ensure numberic types
    df["current_price"] = df["current_price"].astype(float)
    df["market_cap"] = df["market_cap"].astype(float)
    df["total_volume"] = df["total_volume"].astype(float)

    df = df.drop_duplicates(subset=["symbol"])

    expect_cols = ["symbol", "current_price", "market_cap", "total_volume", "ingested_at"]
    assert all(col in df.columns for col in expect_cols), f"Missing expected columns: {expect_cols}"
    
    return df