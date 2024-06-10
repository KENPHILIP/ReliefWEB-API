import json
import requests

# ReliefWeb API endpoint
url = "https://api.reliefweb.int/v1/disasters"

# ICPAC countries
icpac_countries = [
    "Burundi",
    "Djibouti",
    "Eritrea",
    "Ethiopia",
    "Kenya",
    "Rwanda",
    "Somalia",
    "South Sudan",
    "Sudan",
    "Uganda",
    "Tanzania",
]

def fetch_disaster_data():
    # Prepare the payload for the POST request
    payload = {
        "filter": {"operator": "OR", "conditions": []},
        "fields": {"include": ["id", "name", "country", "date", "description"]},
        "limit": 100,
        "sort": ["date.created:desc"],
    }

    # Add conditions for each country
    for country in icpac_countries:
        payload["filter"]["conditions"].append({"field": "country.name", "value": country})

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # POST request
    response = requests.post(url, headers=headers, json=payload, timeout=60)

    if response.status_code == 200:
        disaster_data = response.json()
        return disaster_data.get("data", [])
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    data = fetch_disaster_data()
    print(json.dumps(data, indent=2))
