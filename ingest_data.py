import pandas as pd
from opensky_api import OpenSkyApi
from openSky_api import openSky_api_access 
from postgres_functions import get_connection, insert_airports



# collect data from openSKY api
# arrivals, departures = openSky_api_access()
# df = pd.DataFrame(arrivals)
# print(df) 
# df2 = pd.DataFrame(departures)
# print(df2) 

# csv_name = 'atfm_slot_adherence_2024.csv'
'''connect to postgres'''
conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
    # insert_airports()
else:
    print("Connection to the PostgreSQL encountered and error.")


conn.close()   



if __name__ == "__main__":
    get_connection()