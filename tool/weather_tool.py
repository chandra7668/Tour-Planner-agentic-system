import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("weather_api_key")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    return f"{weather}, {temperature}°C"