import pandas as pd
import configparser
from time import time
from sqlalchemy import create_engine
import psycopg2

config = configparser.ConfigParser()
config.read('config.txt')

csv_name = 'atfm_slot_adherence_2024.csv'

user = config.get('postgres', 'user')
password = config.get('postgres', 'password')
host = config.get('postgres', 'host')
port = config.get('postgres', 'port')
db = config.get('postgres', 'db')
table_name = config.get('postgres', 'table_name')

postgres_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
engine = create_engine(postgres_url)
df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

df = next(df_iter)

df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

df.to_sql(name=table_name, con=engine, if_exists='append')


while True: 

    try:
        t_start = time()
        df = next(df_iter)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = time()
        print('inserted another chunk, took %.3f second' % (t_end - t_start))
    except StopIteration:
        print("Finished ingesting data into the postgres database")
        break

