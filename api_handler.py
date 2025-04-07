# api_handler.py

import requests
from data_store import get_from_cache, save_to_cache, add_to_history

API_KEY = "1e2b3f32571c5fcaa080574a7efb7102"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city, use_cache=True):
    add_to_history(city)

    if use_cache:
        cached_data = get_from_cache(city)
        if cached_data:
            print(f"Loaded cached weather data for {city}.")
            return cached_data

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        save_to_cache(city, weather_data)
        return weather_data

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"City '{city}' not found.")
        else:
            print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return None
