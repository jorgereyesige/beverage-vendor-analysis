import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

#Process to load raw data in chunks to avoid crashes due to insufficient memory

def load_raw_data():
    start = time.time()

    for file in os.listdir('raw'):
        if file.endswith('.csv'):

            first_chunk = True

            for chunk in pd.read_csv(
                f'raw/{file}',
                chunksize=50000,
                low_memory=True
            ):

                chunk.to_sql(
                    file[:-4],  
                    engine,
                    if_exists='replace' if first_chunk else 'append',
                    index=False
                )

                first_chunk = False

            logging.info(f'Ingested {file} into database')

    end = time.time()
    total_time = (end - start) / 60

    logging.info('Ingestion Complete')
    logging.info(f'Total time taken: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()