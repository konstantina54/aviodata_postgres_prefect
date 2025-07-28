import requests
import configparser
import pandas as pd
from math import radians, sin, cos, sqrt, atan2, asin



config = configparser.ConfigParser()
config.read('config.txt')


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        # get_ip_location(response.text)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"



def get_ip_location(ip_address):
    try:
        api = config.get('ipify', 'api')
        url = f"https://geo.ipify.org/api/v2/country,city?apiKey={api}&ipAddress={ip_address}"
        response = requests.get(url, timeout=5)
        data = response.json()
        # data = {'ip': '82.1.26.218', 'location': {'country': 'GB', 'region': 'England', 'city': 'Beckenham', 'lat': 51.40878, 'lng': -0.02526, 'postalCode': 'BR3', 'timezone': '+01:00', 'geonameId': 2656065}, 'as': {'asn': 5089, 'name': 'NTL', 'route': '82.0.0.0/14', 'domain': 'http://www.virginmedia.com', 'type': 'Cable/DSL/ISP'}, 'isp': 'Virgin Media'}
        if 'error' in data:
            return f"Error: {data.get('reason', 'Unknown error')}"
        
        location_data = {
            "ip": data.get("ip"),
            "city": data.get("location", {}).get("city", {}),
            "region": data.get("location", {}).get("region", {}),
            "country": data.get("location", {}).get("country", {}),
            "latitude": data.get("location", {}).get("lat", {}),
            "longitude": data.get("location", {}).get("lng", {}),
            "postCode": data.get("location", {}).get("postalCode", {}),
            "geonameId": data.get("location", {}).get("geonameId",{}),
            "asn": data.get("as", {}).get("asn",{})
        }
        # print(location_data)
        df = pd.DataFrame([location_data])
        # print(df)
        return df

    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"        



def haversin_distance_calculator(personal_coord, coordinates):
    lat1 = personal_coord[0]
    lon1 = personal_coord[1]
    print(lat1, lon1)
# Calculate distance between current location and airport. If raius > than xkm don't bother else identify
# Haversine formula to calculate distance between two lat/lon points in km
# def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    for lat2, lon2 in coordinates:
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        distance = R*c
        if distance < 50:
            print(distance)
        # return distance


if __name__ == "__main__":
    get_public_ip()






