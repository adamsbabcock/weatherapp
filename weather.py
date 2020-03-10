import requests
from settings import API_KEY


def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = "{}appid={}&q={}&units=imperial".format(base_url, API_KEY, city_name)
    response = requests.get(complete_url).json()
    url_not_found = "404"
    data = {}

    if response["cod"] != url_not_found:
        weather_stats = response["main"]
        data["current_temperature"] = weather_stats["temp"]
        data["current_pressure"] = weather_stats["pressure"]
        data["current_humidity"] = weather_stats["humidity"]
        data["weather_description"] = ' and '.join(x['description'] for x in response['weather'])
    else:
        data["error"] = "City Not Found"

    return data
