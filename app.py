import requests, json


api_key = "ADD API KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter City Name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial"
response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in Fahrenheit) = " +
          str(current_temperature) +
          "\n Atmospheric Pressure (in Hpa Unit) = " +
          str(current_pressure) +
          "\n Humidity (in percentage) = " +
          str(current_humidiy) +
          "\n Description = " +
          str(weather_description))

else:
    print(" City Not Found ")
