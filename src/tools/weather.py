import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_weather(city_name: str):
    """
    Fetches real-time weather data using OpenWeather API (Free Plan).
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        condition = weather_data["weather"][0]["description"].capitalize()
        wind_speed = weather_data["wind"]["speed"]

        # print(f"\n🌍 City: {city}, {country}")
        # print(f"🌡️ Temperature: {temperature}°C")
        # print(f"💧 Humidity: {humidity}%")
        # print(f"🌤️ Condition: {condition}")
        # print(f"💨 Wind Speed: {wind_speed} m/s")

        return {
            "city": city,
            "country": country,
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition,
            "wind_speed": wind_speed,
        }

    else:
        return f"Error: Could not fetch weather data for '{city_name}'."