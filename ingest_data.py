import pandas as pd
from opensky_api import OpenSkyApi
from openSky_api import openSky_api_access 
from postgres_functions import insert_airports, insert_ip_safely, db_config, add_ip_data, get_airports_by_region
from get_location import get_public_ip, get_ip_location, haversin_distance_calculator



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
    # insert_ip_safely(ip_address, db_config)
    ip_location_df = get_ip_location(ip_address)
    # add_ip_data(ip_location_df)
    region = ip_location_df['country'].iloc[0]
    personal_coord = [ip_location_df['latitude'].iloc[0], ip_location_df['longitude'].iloc[0]]
    # need to get just the long and lat for my location and for any airport for my region and pass for radius calculation
    airports_data = get_airports_by_region(region)
    arrivals, departures = haversin_distance_calculator(personal_coord, airports_data)
    total = arrivals + departures
    print(f"For yester day there is {arrivals} arrivals and {departures} departures total of {total} for the day in 100km distance")



if __name__ == "__main__":
    main()