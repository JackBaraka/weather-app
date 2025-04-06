# app.py
from api_handler import get_current_weather

def display_weather(weather_data):
    """Format and display weather information"""
    if not weather_data:
        print("No weather data to display")
        return
        
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    condition = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    print("\n" + "="*40)
    print(f"Weather in {city}, {country}")
    print("="*40)
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*40 + "\n")

def main():
    print("Welcome to BARAKA Weather App!")
    
    while True:
        print("\nOptions:")
        print("1. Get current weather")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            city = input("Enter city name: ")
            
            # Ensure the city name is not empty
            if not city.strip():
                print("City name cannot be empty.")
                continue
                
            print("Fetching weather data...")
            weather_data = get_current_weather(city)
            
            if weather_data:
                display_weather(weather_data)
            else:
                print(f"Could not retrieve weather data for {city}.")
        elif choice == "2":
            print("Thank you for using BARAKA Weather App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
