from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

conn_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT"))
}


class CoinResponse(BaseModel):
    symbol: str
    current_price: float
    market_cap: float
    total_volume: float
    ingested_at: datetime


def get_connection():
    return psycopg2.connect(**conn_params)


@app.get("/")
def root():
    return {"message": "Crypto Data API running"}


@app.get("/coins", response_model=list[CoinResponse])
def get_coins():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT symbol, current_price, market_cap, total_volume, ingested_at
            FROM crypto_prices
            ORDER BY market_cap DESC
            """
        )

        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [CoinResponse(symbol=r[0], current_price=r[1], market_cap=r[2], total_volume=r[3], ingested_at=r[4]) for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/coins/{symbol}", response_model=CoinResponse)
def get_coin(symbol: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT symbol, current_price, market_cap, total_volume, ingested_at
            FROM crypto_prices
            WHERE symbol = %s
            """,
            (symbol.lower(),)
        )

        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row is None:
            raise HTTPException(status_code=404, detail=f"Coin '{symbol}' not found")

        return CoinResponse(symbol=row[0], current_price=row[1], market_cap=row[2], total_volume=row[3], ingested_at=row[4])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))