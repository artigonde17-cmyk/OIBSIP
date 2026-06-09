import requests
import os

# Use environment variable (recommended)
API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_API_KEY")


# ---------------- CURRENT WEATHER ----------------
def get_weather(city):

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        r = requests.get(url, timeout=5)
        data = r.json()

        # check API response
        if data.get("cod") != 200:
            return None

        return data

    except:
        return None


# ---------------- 5 DAY FORECAST ----------------
def get_forecast(city):

    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        r = requests.get(url, timeout=5)
        data = r.json()

        # forecast API returns "200" as string
        if data.get("cod") != "200":
            return None

        return data

    except:
        return None