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
- Automated data collection every hour via a scheduler
- Query stored data via a FastAPI REST service
- Automatic API documentation with Swagger UI

## Quick Start (Docker)

```bash
cp .env.example .env   # fill in your credentials
docker compose up --build
```

This starts three services:
- **db** — PostgreSQL (schema applied automatically)
- **api** — FastAPI on `http://localhost:8000`
- **scheduler** — runs the pipeline immediately, then every hour

API docs available at `http://localhost:8000/docs`

## Manual Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your database credentials
3. Install dependencies: `pip install -r requirements.txt`
4. Apply the database schema: `psql -d your_db -f database/schema.sql`
5. Run the pipeline: `python data_pipeline/load.py`
6. Start the API: `uvicorn api.main:app --reload`

## Running Tests

```bash
pytest tests/ -v
```

## API Endpoints

### Get all cryptocurrencies
`GET /coins` — Returns all stored cryptocurrencies ordered by market capitalization.

### Get a specific coin
`GET /coins/{symbol}` — Returns market data for a specific cryptocurrency.

Example:
`GET /coins/btc`

Interactive API documentation available at `/docs`

## Tech Stack

- Python
- Pandas
- FastAPI
- PostgreSQL
- Docker
- APScheduler
- pytest

## Project Structure

```
crypto-data-engineering-pipeline
├ api
│ └ main.py             # FastAPI service exposing crypto data
│
├ data_pipeline
│ ├ ingest.py           # Fetch data from CoinGecko API
│ ├ transform.py        # Data cleaning and transformation
│ ├ load.py             # Load data into PostgreSQL
│ └ scheduler.py        # Automated pipeline (runs every hour)
│
├ database
│ └ schema.sql          # Database schema
│
├ tests
│ └ test_transform.py   # Unit tests for transform layer
│
├ Dockerfile
├ docker-compose.yml
└ README.md
```

## Learning Goals

This project was created to practice **core Data Engineering concepts**, including:

- API data ingestion
- ETL pipeline design
- working with DataFrames
- relational database storage
- building a data access API
- containerized data services
- automated scheduling
- unit testing

## Acknowledgements

Built with assistance from [Claude Code](https://claude.ai/claude-code) (Anthropic) — used for code review, refactoring, and improvements to the API layer.
