import os
import requests
import dotenv
dotenv.load_dotenv()

def convert_keys(obj):
    """Convert keys with hyphens to underscores in nested dictionaries."""
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_key = key.replace('-', '_') if isinstance(key, str) else key
            new_dict[new_key] = convert_keys(value)
        return new_dict
    elif isinstance(obj, list):
        return [convert_keys(item) for item in obj]
    else:
        return obj

def get_data(location):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q={location}&aqi=yes")
    if response.status_code == 200:
        return convert_keys(response.json())
    return {"error":"location not found"}