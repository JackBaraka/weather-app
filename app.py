# app.py

from api_handler import get_current_weather
from data_store import add_to_favorites, get_favorites, get_history
from datetime import datetime

def display_weather(weather_data):
    if not weather_data:
        print("No weather data to display.")
        return
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    condition = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print("\n" + "=" * 40)
    print(f"Weather in {city}, {country}")
    print("=" * 40)
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("=" * 40 + "\n")

    choice = input("Add this city to favorites? (y/n): ")
    if choice.lower() == 'y':
        add_to_favorites(city)
        print(f"{city} added to favorites!")

def display_favorites():
    favorites = get_favorites()
    if not favorites:
        print("No favorite cities yet.")
        return
    print("\nYour Favorite Cities:")
    print("=" * 40)
    for i, city in enumerate(favorites, 1):
        print(f"{i}. {city}")
    print("=" * 40)
    while True:
        choice = input("Enter number to check weather (0 to exit): ")
        if choice == '0':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(favorites):
                weather_data = get_current_weather(favorites[index])
                display_weather(weather_data)
                break
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

def display_history():
    history = get_history()
    if not history:
        print("No search history.")
        return
    print("\nYour Search History:")
    print("=" * 40)
    for i, entry in enumerate(history, 1):
        date_str = datetime.fromtimestamp(entry['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{i}. {entry['city']} - {date_str}")
    print("=" * 40)

def main():
    print("Welcome to the Weather App!")
    while True:
        print("\nOptions:")
        print("1. Get current weather")
        print("2. View favorite cities")
        print("3. View search history")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            city = input("Enter city name: ")
            if not city.strip():
                print("City name cannot be empty.")
                continue
            print("Fetching weather data...")
            weather_data = get_current_weather(city)
            if weather_data:
                display_weather(weather_data)
        elif choice == "2":
            display_favorites()
        elif choice == "3":
            display_history()
        elif choice == "4":
            print("Thanks for using the app. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
