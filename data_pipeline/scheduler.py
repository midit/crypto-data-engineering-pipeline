import os
import logging
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
from ingest import fetch_crypto_data
from transform import transform_crypto_data
from load import load_to_postgres

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def get_conn_params():
    return {
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': int(os.getenv('DB_PORT'))
    }


def run_pipeline():
    logging.info("Pipeline started")
    df = fetch_crypto_data()
    df = transform_crypto_data(df)
    load_to_postgres(df, get_conn_params())
    logging.info("Pipeline completed")


if __name__ == "__main__":
    run_pipeline()

    scheduler = BlockingScheduler()
    scheduler.add_job(run_pipeline, 'interval', hours=1)
    logging.info("Scheduler running — pipeline executes every hour")
    scheduler.start()
