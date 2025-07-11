# import pandas as pd
# import time
# from datetime import datetime
# import requests, json
from opensky_api import OpenSkyApi
from openSky_api import openSky_api_access 
# from postgres_functions import get_connection


# config = configparser.ConfigParser()
# config.read('config.txt')

csv_name = 'atfm_slot_adherence_2024.csv'

# conn = get_connection()
# if conn:
#     print("Connection to the PostgreSQL established successfully.")
# else:
#     print("Connection to the PostgreSQL encountered and error.")


# conn.close()    

# arrivals + departures

# Find more data from the web. Use the small file to showcase normalization and
# data restructioring.

# df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

# df = next(df_iter)

# df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

# df.to_sql(name=table_name, con=engine, if_exists='append')


# while True: 

#     try:
#         t_start = time()
#         df = next(df_iter)
#         df.to_sql(name=table_name, con=engine, if_exists='append')
#         t_end = time()
#         print('inserted another chunk, took %.3f second' % (t_end - t_start))
#     except StopIteration:
#         print("Finished ingesting data into the postgres database")
#         break

if __name__ == "__main__":
    openSky_api_access()