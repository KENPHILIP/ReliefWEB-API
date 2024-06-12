import requests
import pandas as pd
from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt  # Import Matplotlib
import io
import base64
from vega_datasets import data

app = Flask(__name__,template_folder="templates")

# List of ICPAC countries
icpac_countries = ["Burundi", "Djibouti", "Eritrea", "Ethiopia", "Kenya",
                   "Rwanda", "Somalia", "South Sudan", "Sudan", "Uganda", "Tanzania"]

# ReliefWeb API URL
url = "https://api.reliefweb.int/v1/disasters"

def fetch_disaster_data():
    # Construct filter conditions
    conditions = [{"field": "country.name.exact", "value": country} for country in icpac_countries]
    filter_conditions = {
        "operator": "OR",
        "conditions": conditions
    }

    payload = {
        "filter": filter_conditions,
        "limit": 100,
        "sort": ["date:desc"]
    }

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        disaster_data = response.json().get("data", [])
        return disaster_data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {str(e)}")
        return []

@app.route('/')
def index():
    return render_template('plot_view.html')

@app.route('/data')
def get_data():
    disaster_data = fetch_disaster_data()
    return jsonify(disaster_data)

@app.route('/plot')
def generate_plot():
    # Fetch disaster data
    disaster_data = fetch_disaster_data()

    # Prepare data for plotting
    countries = []
    num_disasters = []

    for disaster in disaster_data:
        fields = disaster.get('fields', {})
        if 'country' in fields and 'name' in fields['country']:
            country_name = fields['country']['name']
            if country_name in icpac_countries:
                countries.append(country_name)
                num_disasters.append(1)  # Increment for each disaster

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(countries, num_disasters)
    plt.xlabel('Countries')
    plt.ylabel('Number of Disasters')
    plt.title('Number of Disasters by Country')
    plt.xticks(rotation=45)
    
    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Encode plot to base64 string
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('plot.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
