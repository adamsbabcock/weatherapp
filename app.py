import requests
from settings import API_KEY


base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter City Name : ")
complete_url = "{}appid={}&q={}&units=imperial".format(base_url, API_KEY, city_name)
response = requests.get(complete_url).json()
URL_NOT_FOUND = "404"

if response["cod"] != URL_NOT_FOUND:
    weather_stats = response["main"]
    current_temperature = weather_stats["temp"]
    current_pressure = weather_stats["pressure"]
    current_humidity = weather_stats["humidity"]
    weather_description = ' and '.join([x['description'] for x in response['weather']])
    print(
        "Temperature = {}\u00b0F \nAtmospheric Pressure = {} hPa \nHumidity = {}% "
        "\nDescription = {} ".format(current_temperature, current_pressure, current_humidity, weather_description.title())
    )
else:
    print(" City Not Found ")
