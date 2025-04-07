# data_store.py
import os
import json
from datetime import datetime, timedelta

# Constants
DATA_DIR = "data"
CACHE_FILE = os.path.join(DATA_DIR, "weather_cache.json")
FAVORITES_FILE = os.path.join(DATA_DIR, "favorites.json")
HISTORY_FILE = os.path.join(DATA_DIR, "search_history.json")
CACHE_EXPIRY = 30  # minutes

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_to_cache(city, weather_data):
    ensure_data_dir()
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            try:
                cache = json.load(f)
            except json.JSONDecodeError:
                cache = {}
    weather_data['_timestamp'] = datetime.now().timestamp()
    cache[city.lower()] = weather_data
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def get_from_cache(city):
    if not os.path.exists(CACHE_FILE):
        return None
    with open(CACHE_FILE, 'r') as f:
        try:
            cache = json.load(f)
        except json.JSONDecodeError:
            return None
    city_data = cache.get(city.lower())
    if not city_data:
        return None
    timestamp = city_data.get('_timestamp')
    if timestamp:
        cache_time = datetime.fromtimestamp(timestamp)
        if datetime.now() - cache_time > timedelta(minutes=CACHE_EXPIRY):
            return None
    return city_data

def add_to_favorites(city):
    ensure_data_dir()
    favorites = []
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r') as f:
            try:
                favorites = json.load(f)
            except json.JSONDecodeError:
                favorites = []
    if city.lower() not in [fav.lower() for fav in favorites]:
        favorites.append(city)
    with open(FAVORITES_FILE, 'w') as f:
        json.dump(favorites, f, indent=2)

def get_favorites():
    if not os.path.exists(FAVORITES_FILE):
        return []
    with open(FAVORITES_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def add_to_history(city):
    ensure_data_dir()
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    entry = {'city': city, 'timestamp': datetime.now().timestamp()}
    history.append(entry)
    if len(history) > 10:
        history = history[-10:]
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
