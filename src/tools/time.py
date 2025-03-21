import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()


def get_time_info(city_name: str):
    """Fetch latitude, longitude, and time zone information from a city name."""
    
    # Step 1: Get Latitude & Longitude
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={os.getenv('GOOGLE_MAPS_API_KEY')}"
    geocode_response = requests.get(geocode_url).json()

    if geocode_response["status"] != "OK":
        # print(f"Error in Geocoding: {geocode_response['status']}")
        return f"Error in Geocoding: {geocode_response['status']}"

    location = geocode_response["results"][0]["geometry"]["location"]
    lat, lon = location["lat"], location["lng"]

    # Step 2: Get Time Zone Information
    timestamp = int(datetime.datetime.utcnow().timestamp())
    timezone_url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key={os.getenv('GOOGLE_MAPS_API_KEY')}"
    timezone_response = requests.get(timezone_url).json()

    if timezone_response["status"] != "OK":
        # print(f"Error in Time Zone API: {timezone_response['status']}")
        return f"Error in Time Zone API: {timezone_response['status']}"

    time_zone_id = timezone_response["timeZoneId"]
    time_zone_name = timezone_response["timeZoneName"]
    raw_offset = timezone_response["rawOffset"] 
    dst_offset = timezone_response["dstOffset"]
    local_offset = raw_offset + dst_offset
    local_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=local_offset)

    # print(f"📍 City: {city_name}")
    # print(f"🌍 Coordinates: ({lat}, {lon})")
    # print(f"🕒 Time Zone ID: {time_zone_id}")
    # print(f"⏳ Time Zone Name: {time_zone_name}")
    # print(f"⏰ Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

    return {
        "city": city_name,
        "latitude": lat,
        "longitude": lon,
        "time_zone_id": time_zone_id,
        "time_zone_name": time_zone_name,
        "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S')
    }