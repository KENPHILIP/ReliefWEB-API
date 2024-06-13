import pandas as pd
import altair as alt
from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from geopy.geocoders import Nominatim
from flask import Flask, render_template
from markupsafe import Markup
import json

# Load processed disaster data
disaster_data = pd.read_csv(r"D:\confidentials\GCP lessons\Solara\processed_disasters_data.csv")

# Debug: Print column names to ensure 'country' exists
print("Columns in disaster_data:", disaster_data.columns)

# Check if 'country' column exists
if 'country' not in disaster_data.columns:
    raise KeyError("The column 'country' is not found in the disaster data.")

# Initialize geolocator
geolocator = Nominatim(user_agent="disaster_prediction_app")

def get_coordinates(place_name):
    try:
        location = geolocator.geocode(place_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)
    except Exception as e:
        print(f"Error geocoding {place_name}: {e}")
        return (None, None)

# Apply reverse geocoding to country names
disaster_data[['latitude', 'longitude']] = disaster_data['country'].apply(lambda x: pd.Series(get_coordinates(x)))

# Drop rows with missing coordinates
disaster_data.dropna(subset=['latitude', 'longitude'], inplace=True)

# Example training code (replace with actual model training)
X = disaster_data[['year', 'day', 'month', 'latitude', 'longitude']]  # Features including coordinates
y = disaster_data['disaster_type']  # Target column for prediction

# Train RandomForestClassifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X, y)

# Save the trained model
model_filename = 'random_forest_model.joblib'
dump(rf_classifier, model_filename)
print("Model saved successfully as", model_filename)

# Make predictions and add them to the disaster_data DataFrame
disaster_data['prediction'] = rf_classifier.predict(X)

# Load GeoJSON file for East Africa shape
with open(r"D:\confidentials\GCP lessons\Solara\shapefiles\ea_ghcf_simple.json") as f:
    east_africa_geojson = json.load(f)

# Altair chart for disaster map visualization
map_chart = alt.Chart(alt.Data(values=east_africa_geojson)).mark_geoshape(
    fill='lightgray',
    stroke='white'
).encode(
    tooltip=[alt.Tooltip('properties.name:N', title='Country')]
).project(
    type='mercator'
).properties(
    width=600,
    height=400,
    title='Disaster Predictions in East Africa'
).interactive()

# Overlay disaster points
points_chart = alt.Chart(disaster_data).mark_circle(size=100).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color=alt.Color('prediction:N', legend=alt.Legend(title="Predictions")),
    tooltip=['country:N', 'prediction:N', 'year:O', 'month:O', 'day:O']
)

# Combine the map and points chart
final_chart = (map_chart + points_chart).configure_legend(
    orient='right',
    titleFontSize=13,
    labelFontSize=12
)

# Debug: Print chart HTML
chart_html = final_chart.to_html()
print(chart_html)  # This should print the HTML for the chart

# Flask app setup
app = Flask(__name__)

# Route for serving the Solara dashboard HTML page
@app.route('/')
def index():
    return render_template('map_view.html', chart=Markup(chart_html))

# Main script entry point
if __name__ == "__main__":
    app.run(port=9090)  # Adjust port number as needed
