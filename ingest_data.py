import pandas as pd
from opensky_api import OpenSkyApi
from openSky_api import openSky_api_access 
from postgres_functions import insert_airports, insert_ip_safely, db_config, add_ip_data
from get_location import get_public_ip, get_ip_location



# collect data from openSKY api
# arrivals, departures = openSky_api_access()
# df = pd.DataFrame(arrivals)
# print(df) 
# df2 = pd.DataFrame(departures)
# print(df2) 


def main():
    # insert_airports()
    ip_address = get_public_ip()
    # ip_address = True
    insert_ip_safely(ip_address, db_config)
    ip_location_df = get_ip_location(ip_address)
    # need to get just the long and lat for my location and for any airport for my region and pass for radius calculation
    add_ip_data(ip_location_df)



if __name__ == "__main__":
    main()