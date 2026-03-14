from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn_params = {
    "host": "localhost",
    "database": "crypto_db",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**conn_params)


@app.get("/")
def root():
    return {"message": "Crypto Data API running"}


@app.get("/coins")
def get_coins():

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

    return rows

@app.get("/coins/{symbol}")
def get_coin(symbol: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT symbol, current_price, market_cap, total_volume, ingested_at
        FROM crypto_prices
        WHERE symbol = %s
        """,
        (symbol,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return row