import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse # for command line argument parsing

import os # to handle file operations WTF IS OS USED FOR ?

def main(params):

    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    ## WTF IS THIS FOR
    parquet_name = 'output.parquet'
    os.system(f"wget {url} -O {parquet_name}") # gets file from url and writes it to parquet_name file

    ## ENGINE

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}') 
    engine.connect()

    ## DATA INGESTION
    df_parquet = pd.read_parquet(parquet_name)
    df_parquet.to_csv("yellow_tripdata_2021-01_converted_to_csv", index=False)

    df_iter = pd.read_csv("yellow_tripdata_2021-01_converted_to_csv", iterator=True, chunksize=100000)

    df_chunk = next(df_iter)

    df_chunk["tpep_pickup_datetime"] = pd.to_datetime(df_chunk["tpep_pickup_datetime"])
    df_chunk["tpep_dropoff_datetime"] = pd.to_datetime(df_chunk["tpep_dropoff_datetime"])

    df_chunk.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df_chunk.to_sql(name=table_name, con=engine, if_exists="append")


    for df_chunk in df_iter:
        t_start = time()

        df_chunk["tpep_pickup_datetime"] = pd.to_datetime(df_chunk["tpep_pickup_datetime"])
        df_chunk["tpep_dropoff_datetime"] = pd.to_datetime(df_chunk["tpep_dropoff_datetime"])
        df_chunk.to_sql(name=table_name, con=engine, if_exists="append")


        t_end = time()
        
        print("inserted another chunk..., took %.3f second" % (t_end - t_start))

#################################################

if __name__ == "__main__":

    ## Argparse setup
    # Using argparse to handle command line arguments for PostgreSQL connection details and CSV file URL
    # It allows users to specify the database connection parameters and the URL of the CSV file to be ingested into PostgreSQL.

    # We will use argparse to handle the following command line arguments:
    # Username
    # Password
    # Host
    # Port
    # Database name
    # Table name
    # URL for the CSV file

    parser = argparse.ArgumentParser(description="PIngest CSV data into PostgreSQL") # description will be printed in help

    # user, password, host, port, database name, table name, url for the CSV file
    parser.add_argument("--user", type=str, required=True, help="PostgreSQL username")
    parser.add_argument("--password", type=str, required=True, help="PostgreSQL password")
    parser.add_argument("--host", type=str, required=True, help="PostgreSQL host")
    parser.add_argument("--port", type=int, required=True, help="PostgreSQL port")
    parser.add_argument("--db", type=str, required=True, help="PostgreSQL database name")
    parser.add_argument("--table_name", type=str, required=True, help="PostgreSQL table name")
    parser.add_argument("--url", type=str, required=True, help="URL for the CSV file")

    args = parser.parse_args()
    main(args)

