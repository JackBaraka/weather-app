# test_api.py

from api_handler import get_current_weather

def test_api():
    city = "London"
    weather_data = get_current_weather(city)
    
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Condition: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Failed to retrieve weather data")

if __name__ == "__main__":
    test_api()
