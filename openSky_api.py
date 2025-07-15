from opensky_api import OpenSkyApi
import configparser
import time
from datetime import datetime
import requests, json


config = configparser.ConfigParser()
config.read('config.txt')


def openSky_api_access():
    client_id = config.get('openSky', 'client_id')
    client_secret = config.get('openSky', 'client_secret')

    token_url = 'https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, data=data)
    access_token = response.json()['access_token']
    airport = 'EDDF'
    begin = int(time.mktime(time.strptime('2025-07-09 12:00', '%Y-%m-%d %H:%M')))
    end = int(time.mktime(time.strptime('2025-07-09 14:00', '%Y-%m-%d %H:%M')))
    headers = {'Authorization': f'Bearer {access_token}'}
    arrivals = openSky_arrival(headers, airport, begin, end)
    departures = openSky_departures(headers, airport, begin, end)
    return arrivals, departures

  

def openSky_arrival(headers, airport, begin, end):
    url = f'https://opensky-network.org/api/flights/arrival?airport={airport}&begin={begin}&end={end}'
    response = requests.get(url, headers=headers)
    arrivals = response.json()
    return arrivals

def openSky_departures(headers, airport, begin, end):
    url = f'https://opensky-network.org/api/flights/departure?airport={airport}&begin={begin}&end={end}'
    response = requests.get(url, headers=headers)
    departures = response.json()
    return departures
