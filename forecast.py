import os
import requests
from datetime import datetime


def main():
    key = os.environ.get('WEATHER_KEY')
    query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()

    forecast_items = data['list']

    for forecast in forecast_items:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        print(f'at {date} temp is {temp}')



