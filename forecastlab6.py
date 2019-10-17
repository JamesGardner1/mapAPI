''' This program will all the user to enter a city with country 
and display a forecast of weather metrics for 5 days '''
import os
import requests
from datetime import datetime


def main():
    location = get_location()
    data = get_forecast(location)
    get_metrics(data)


def get_location():
    ''' Retrieve the location '''
    location = input('Please provide a city and country code you would like to know the forecast in: ')
    if ' ' in location:
        print('Please enter the city and country in this format : \'minneapolis,us\'')
    else:
        return location


def get_forecast(location):
    key = os.environ.get('WEATHER_KEY')
    query = {'q': location, 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    return data

def get_metrics(data):
    key = os.environ.get('WEATHER_KEY')
    forecast_items = data['list']
    for forecast in forecast_items:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        weather_description = data['weather'][0]['description']
        wind = data['wind']['speed']
        print(f'In {location} it is {temp}')

        


if __name__ == '__main__':
    main()