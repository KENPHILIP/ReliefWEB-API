import requests

url = "https://api.reliefweb.int/v1/disasters"

# List of ICPAC countries
icpac_countries = ["Burundi", "Djibouti", "Eritrea", "Ethiopia", "Kenya",
                   "Rwanda", "Somalia", "South Sudan", "Sudan", "Uganda", "Tanzania"]

# Construct filter conditions
conditions = [{"field": "country", "value": country} for country in icpac_countries]
filter_conditions = {
    "operator": "OR",
    "conditions": conditions
}

payload = {
    "filter": filter_conditions,
    "fields": {"include": ["id", "name", "country", "date", "description"]},
    "limit": 100,
    "sort": ["date:desc"]
}

def fetch_disaster_data():
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        disaster_data = response.json()
        return disaster_data.get("data", [])
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to retrieve data: {str(e)}")

# Example usage
if __name__ == "__main__":
    disaster_data = fetch_disaster_data()
    # Print out the structure of the fetched data
    print(disaster_data)
