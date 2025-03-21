import requests

def get_country_info(country_name: str):
    """
    Fetches country details from the RestCountries API.
    - country_name: Name of the country (e.g., "Japan", "France")
    """

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()[0] 
        name = country_data.get("name", {}).get("common", "Unknown")
        capital = country_data.get("capital", ["Unknown"])[0]
        population = country_data.get("population", "Unknown")
        region = country_data.get("region", "Unknown")
        subregion = country_data.get("subregion", "Unknown")
        currency = list(country_data.get("currencies", {}).keys())[0] if "currencies" in country_data else "Unknown"
        languages = ", ".join(country_data.get("languages", {}).values()) if "languages" in country_data else "Unknown"
        flag = country_data.get("flags", {}).get("png", "")

        # print(f"\n🌍 Country: {name}")
        # print(f"🏛️ Capital: {capital}")
        # print(f"👥 Population: {population}")
        # print(f"🌎 Region: {region}, {subregion}")
        # print(f"💰 Currency: {currency}")
        # print(f"🗣️ Languages: {languages}")
        # print(f"🏴 Flag: {flag}")

        return {
            "country": name,
            "capital": capital,
            "population": population,
            "region": region,
            "subregion": subregion,
            "currency": currency,
            "languages": languages,
            "flag": flag,
        }

    else:
        # print(f"Error: Could not fetch data for '{country_name}'")
        return f"Error: Could not fetch data for '{country_name}'"

