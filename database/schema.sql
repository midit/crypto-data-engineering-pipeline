-- schema.sql
CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    current_price NUMERIC(20,2) NOT NULL,
    market_cap NUMERIC(20,2) NOT NULL,
    total_volume NUMERIC(20,2) NOT NULL,
    ingested_at TIMESTAMP NOT NULL
);