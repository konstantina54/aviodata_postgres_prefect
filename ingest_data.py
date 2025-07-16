import pandas as pd
from opensky_api import OpenSkyApi
from openSky_api import openSky_api_access 
from postgres_functions import insert_airports, insert_ip_safely, db_config
from get_location import get_public_ip



# collect data from openSKY api
# arrivals, departures = openSky_api_access()
# df = pd.DataFrame(arrivals)
# print(df) 
# df2 = pd.DataFrame(departures)
# print(df2) 


def main():
    insert_airports()
    ip_address = get_public_ip()
    insert_ip_safely(ip_address, db_config)




if __name__ == "__main__":
    main()