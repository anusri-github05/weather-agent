import requests


def get_coordinates(city):
    """
    Gets the latitude and longitude of a city using Open-Meteo Geocoding API.
    """

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search?"
        f"name={city}&count=1"
    )
            
    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch coordinates."

    data = response.json()

    if "results" not in data:
        return "City not found."

    location = data["results"][0]

    return {
        "city": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):
    """
    Gets the current weather from Open-Meteo.
    """

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch weather."

    data = response.json()

    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"]
    }