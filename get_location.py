import requests
import configparser


config = configparser.ConfigParser()
config.read('config.txt')


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        get_ip_location(response.text)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"



def get_ip_location(ip_address):
    try:
        api = config.get('ipify', 'api')
        # url = f"https://geo.ipify.org/api/v2/country,city?apiKey={api}&ipAddress={ip_address}"
        # response = requests.get(url, timeout=5)
        # data = response.json()
        data = {'ip': '82.1.26.218', 'location': {'country': 'GB', 'region': 'England', 'city': 'Beckenham', 'lat': 51.40878, 'lng': -0.02526, 'postalCode': 'BR3', 'timezone': '+01:00', 'geonameId': 2656065}, 'as': {'asn': 5089, 'name': 'NTL', 'route': '82.0.0.0/14', 'domain': 'http://www.virginmedia.com', 'type': 'Cable/DSL/ISP'}, 'isp': 'Virgin Media'}
        if 'error' in data:
            return f"Error: {data.get('reason', 'Unknown error')}"
        
        location_info = {
            "IP": data.get("ip"),
            "City": data.get("location", {}).get("city", {}),
            "Region": data.get("location", {}).get("region", {}),
            "Country": data.get("location", {}).get("country", {}),
            "Latitude": data.get("location", {}).get("lat", {}),
            "Longitude": data.get("location", {}).get("lng", {}),
            "PostCode": data.get("location", {}).get("postalCode", {})
        }
        print(location_info)
        return location_info

    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"        

# print("Your public IP address is:", get_public_ip())

get_public_ip()






