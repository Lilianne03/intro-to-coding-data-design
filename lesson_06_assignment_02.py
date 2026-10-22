import requests

def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url)
    data = response.json()
    if "results" not in data:
        raise Exception("City not found.")
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]
    return latitude, longitude, elevation

def get_weather_forecast(city_name):
    days = []
    temp_max = []
    temp_min = []
    
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return days, temp_max, temp_min
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"  
    url += f"&latitude={latitude:.2f}"  
    url += f"&longitude={longitude:.2f}"  
    url += f"&elevation={elevation:.2f}"  

    url += "&daily=temperature_2m_max,temperature_2m_min"
    url += "&timezone=Europe%2FBerlin"
    url += "&forecast_days=7"

    response = requests.get(url)

    data = response.json()

    days = data["daily"]["time"]
    temp_max = data["daily"]["temperature_2m_max"]
    temp_min = data["daily"]["temperature_2m_min"]

    return days, temp_max, temp_min


if __name__ == "__main__":
    city_name = input("Please enter the name of a city: ")

    while city_name != "exit":
        days, temp_max, temp_min = get_weather_forecast(city_name)
        for index in range(len(days)):
            print(
                f"{days[index]}: "
                f"High: {temp_max[index]}°C, "
                f"Low: {temp_min[index]}°C"
            )

            print()
            city_name = input("Please enter the name of a city: ")