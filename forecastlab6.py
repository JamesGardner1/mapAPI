''' This program will all the user to enter a city with country 
and display a forecast of weather metrics for 5 days '''
import os
import requests
from datetime import datetime






''' Retrieve the location '''
location = input('Please provide a city and country code you would like to know the forecast in: ')

key = os.environ.get('WEATHER_KEY')
query = {'q': location, 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()
forecast_items = data['list']
weather = forecast_items[0]

for forecast in forecast_items:
    timestamp = forecast['dt']
    date = datetime.fromtimestamp(timestamp)
    temp = forecast['main']['temp']
    weather_description = weather['weather'][0]['description']
    wind = weather['wind']['speed']
    print(f'In {location} at {date} it is {weather_description}, the temperature is {temp}, and the wind speed is {wind}')

        


