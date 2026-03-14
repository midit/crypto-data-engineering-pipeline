# Crypto Data Engineering Pipeline

<img width="2084" height="1084" alt="banner" src="https://github.com/user-attachments/assets/aa150547-cc11-40f0-bfd9-0858ee8364ab" />

Small data engineering project that builds a pipeline for collecting and processing cryptocurrency market data.

## Project Goal

The project demonstrates a typical data engineering workflow:

API → ingestion → transformation → storage → API access

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

- Fetch cryptocurrency market data from the CoinGecko API
- Transform and clean raw API data using Pandas
- Store processed data in PostgreSQL
- Query stored data via a FastAPI REST service
- Automatic API documentation with Swagger

# API Endpoints
Example endpoints exposed by the FastAPI service:
### Get all cryptocurrencies 
`GET /coins` — Returns all stored cryptocurrencies ordered by market capitalization.

### Get a specific coin
`GET /coins/{symbol}` — Returns market data for a specific cryptocurrency.

Example:  
`GET /coins/btc`  

Interactive API documentation is available at: `/docs`

## Tech Stack

- Python
- Pandas
- Requests
- FastAPI
- PostgreSQL
- Docker

## Project Structure

```
crypto-data-engineering-pipeline
├ api
│ └ main.py # FastAPI service exposing crypto data
│
├ data_pipeline
│ ├ ingest.py # Fetch data from CoinGecko API
│ ├ transform.py # Data cleaning and transformation
│ └ load.py # Load data into PostgreSQL
│
├ database
│ └ schema.sql # Database schema
│
└ README.md
```

# Learning Goals
This project was created to practice **core Data Engineering concepts**, including:

- API data ingestion
- ETL pipeline design
- working with DataFrames
- relational database storage
- building a data access API
- containerized data services
