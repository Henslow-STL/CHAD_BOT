import requests

def get_weather_description(code):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    return weather_codes.get(code, "Unknown")

cities = [
    {
        "name": "St. Louis",
        "lat": 38.6270,
        "lon": -90.1994
    }, 
    {
        "name": "Milwaukee",
        "lat": 43.0389,
        "lon": -87.9065
    }
]

def get_weather_data(city_name, latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max","temperature_unit": "fahrenheit",
        "timezone": "America/Chicago",
        "forecast_days": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"error fetching weather data for {city_name}): {e}")
        return None

    try:
        weather_data = {
            "city": city_name,
            "temperature": data["current"]["temperature_2m"],
            "humidity": data["current"]["relative_humidity_2m"],
            "high": data["daily"]["temperature_2m_max"][0],
            "low": data["daily"]["temperature_2m_min"][0],
            "weather_code": data["current"]["weather_code"],
            "description": get_weather_description(data["current"]["weather_code"]),
            "rain_chance": data["daily"]["precipitation_probability_max"][0],
            "alert": get_weather_alert({
            "weather_code": data["current"]["weather_code"],
            "rain_chance": data["daily"]["precipitation_probability_max"][0]
        }),

        }
    except KeyError as e:
        print(f"error parsing weather data for {city_name}: {e}")
        return None

    return weather_data

def get_weather_alert(city_data):
    code = city_data["weather_code"]
    rain = city_data["rain_chance"]

    if code >= 95:
        return "⚠️ Thunderstorm Alert"
    elif rain >= 70:
        return "⚠️ High Chance of Rain"
    elif code in [65, 67, 82]:
        return "⚠️ Heavy Rain Alert"
    elif code in [75, 86]:
        return "⚠️ Heavy Snow Alert"
    else:
        return "No severe alerts"
    
def compare_weather(city1, city2):
    comparison = {}

    if city1["temperature"] > city2["temperature"]:
        comparison["warmer_city"] = city1["city"]
    elif city2["temperature"] > city1["temperature"]:
        comparison["warmer_city"] = city2["city"]
    else:
        comparison["warmer_city"] = "Tie"

    if city1["humidity"] > city2["humidity"]:
        comparison["more_humid_city"] = city1["city"]
    elif city2["humidity"] > city1["humidity"]:
        comparison["more_humid_city"] = city2["city"]
    else:
        comparison["more_humid_city"] = "Tie"

    city1_range = city1["high"] - city1["low"]
    city2_range = city2["high"] - city2["low"]

    if city1_range > city2_range:
        comparison["bigger_temp_swing"] = city1["city"]
    elif city2_range > city1_range:
        comparison["bigger_temp_swing"] = city2["city"]
    else:
        comparison["bigger_temp_swing"] = "Tie"

    comparison["city1_temp_range"] = city1_range
    comparison["city2_temp_range"] = city2_range

    return comparison