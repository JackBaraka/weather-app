# api_handler.py (updated)
import requests
from config import API_KEY, BASE_URL

def get_current_weather(city):
    """
    Fetch current weather data for a given city
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        
        # Check for HTTP errors
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors
        
        # Return the JSON data
        return response.json()
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"City '{city}' not found. Please check spelling.")
        else:
            print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Timeout Error: The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return None
