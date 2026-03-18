import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data_pipeline'))

import pytest
import pandas as pd
from transform import transform_crypto_data


def make_df(**kwargs):
    defaults = {
        "symbol": ["btc", "eth"],
        "current_price": [50000.0, 3000.0],
        "market_cap": [1.0, 0.4],
        "total_volume": [0.5, 0.2],
    }
    defaults.update(kwargs)
    return pd.DataFrame(defaults)


def test_adds_ingested_at():
    df = transform_crypto_data(make_df())
    assert "ingested_at" in df.columns


def test_removes_duplicates():
    df = make_df(
        symbol=["btc", "btc", "eth"],
        current_price=[50000.0, 50000.0, 3000.0],
        market_cap=[1.0, 1.0, 0.4],
        total_volume=[0.5, 0.5, 0.2],
    )
    result = transform_crypto_data(df)
    assert len(result) == 2
    assert result["symbol"].nunique() == 2


def test_numeric_types():
    df = make_df(current_price=["50000", "3000"], market_cap=["1.0", "0.4"], total_volume=["0.5", "0.2"])
    result = transform_crypto_data(df)
    assert result["current_price"].dtype == float
    assert result["market_cap"].dtype == float
    assert result["total_volume"].dtype == float


def test_column_names_lowercased():
    df = make_df()
    df.columns = [c.upper() for c in df.columns]
    result = transform_crypto_data(df)
    assert all(c == c.lower() for c in result.columns)


def test_missing_required_column_raises():
    df = make_df().drop(columns=["market_cap"])
    with pytest.raises(Exception):
        transform_crypto_data(df)


def test_does_not_modify_original():
    df = make_df()
    original_len = len(df)
    transform_crypto_data(df)
    assert len(df) == original_len
    assert "ingested_at" not in df.columns
