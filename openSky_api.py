from opensky_api import OpenSkyApi
import configparser
from datetime import datetime, time, timedelta
import requests, json


config = configparser.ConfigParser()
config.read('config.txt')


def openSky_api_access(airport):
    # print(airport)
    client_id = config.get('openSky', 'client_id')
    client_secret = config.get('openSky', 'client_secret')

    token_url = 'https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, data=data)
    response.raise_for_status() 
    access_token = response.json()['access_token']
    yesterday = datetime.today().date() - timedelta(days=1)
    begin = int(datetime.combine(yesterday, time.min).timestamp())
    end = int(datetime.combine(yesterday, time.max).timestamp())
    headers = {'Authorization': f'Bearer {access_token}'}
    arrivals = openSky_arrival(headers, airport, begin, end)
    departures = openSky_departures(headers, airport, begin, end)
    return arrivals, departures

  

def openSky_arrival(headers, airport, begin, end):
    url = f'https://opensky-network.org/api/flights/arrival?airport={airport}&begin={begin}&end={end}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        arrivals = response.json()
        number_arrivals = len(arrivals)
        return number_arrivals
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return 0  # Return empty list or None as preferred
        else:
            print(f"HTTP error: {e}, response: {response.text}")
            raise  # Re-raise unexpected errors


def openSky_departures(headers, airport, begin, end):
    url = f'https://opensky-network.org/api/flights/departure?airport={airport}&begin={begin}&end={end}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        departures = response.json()
        number_departures = len(departures)
        return number_departures
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return 0  # Return empty list or None as preferred
        else:
            print(f"HTTP error: {e}, response: {response.text}")
            raise  # Re-raise unexpected errors
