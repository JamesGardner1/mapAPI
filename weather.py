import requests
import os


key = os.environ.get('WEATHER_KEY')
city = input('What place would you like to know the weather in?')
query = {'q': city, 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/weather'
data = requests.get(url, params=query).json()
weather_description = data['weather'][0]['description']

temp= data['main']['temp']
print(f'The weather is {weather_description}, the temperature is {temp:.2f}F.')

