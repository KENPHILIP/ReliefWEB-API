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

# Print response content
if response.status_code == 200:
    disaster_data = response.json()
    disasters = disaster_data.get("data", [])

    # Print entire response data for inspection
    print(json.dumps(disaster_data, indent=2))

else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print("Response Content:", response.content)

print(disasters[3]["fields"]["description"])
