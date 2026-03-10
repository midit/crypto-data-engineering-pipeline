# Crypto Data Engineering Pipeline

<img width="2084" height="1084" alt="banner" src="https://github.com/user-attachments/assets/aa150547-cc11-40f0-bfd9-0858ee8364ab" />

Small data engineering project that builds a pipeline for collecting and processing cryptocurrency market data.

## Project Goal

Build a simple end-to-end data pipeline:

API → ingestion → transformation → storage → analytics

The project focuses on practicing data engineering concepts such as:

- API data ingestion
- data transformation
- working with dataframes
- storing data in databases
- pipeline structuring

## Data Source

Data is fetched from the CoinGecko API.

https://www.coingecko.com/en/api

## Current Features

- Fetch cryptocurrency market data
- Convert API response into a structured DataFrame

## Planned Features

- Data transformation layer
- Store data in PostgreSQL
- Dockerized pipeline
- Scheduled data collection
- Simple analytics dashboard

## Tech Stack

Python  
Pandas  
CoinGecko API  
PostgreSQL (planned)  
Docker (planned)

## Project Structure

```
crypto-data-engineering-pipeline
│
├── data/
├── notebooks/
├── src/
│   ├── ingest.py
│   └── transform.py (planned)
│
└── README.md
```
