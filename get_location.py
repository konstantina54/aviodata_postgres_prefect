
import requests



def get_ip_location(ip_address):
    try:
        url = f"https://ipapi.co/{ip_address}/json/"
        response = requests.get(url, timeout=5)
        data = response.json()
        print(data)

        if 'error' in data:
            return f"Error: {data.get('reason', 'Unknown error')}"
        
        location_info = {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country_name"),
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
        }

        return location_info



def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        get_ip_location(response.text)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"



print("Your local IP address is:", get_public_ip())




