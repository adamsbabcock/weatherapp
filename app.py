from weather import get_weather


city_name = input("Enter City Name : ")
weather_data = get_weather(city_name)
print(
    "Temperature = {}\u00b0F \nAtmospheric Pressure = {} hPa \nHumidity = {}% "
    "\nDescription = {} ".format(weather_data["current_temperature"],
                                 weather_data["current_pressure"],
                                 weather_data["current_humidity"],
                                 weather_data["weather_description"].title())
)
