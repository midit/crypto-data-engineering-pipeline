import psycopg2
import logging
from ingest import fetch_crypto_data
from transform import transform_crypto_data
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO)

def load_to_postgres(df, conn_params):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO crypto_prices (symbol, current_price, market_cap, total_volume, ingested_at)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (row['symbol'], row['current_price'], row['market_cap'], row['total_volume'], row['ingested_at'])
        )

    conn.commit()
    cursor.close()
    conn.close()
    logging.info("Inserted %d rows into PostgreSQL", len(df))

if __name__ == "__main__":
    df = fetch_crypto_data()
    df = transform_crypto_data(df)

    conn_params = {
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': int(os.getenv('DB_PORT'))
    }

    load_to_postgres(df, conn_params)