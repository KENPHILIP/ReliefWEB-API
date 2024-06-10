from flask import Flask, render_template
import solara_app
import altair as alt
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Function to fetch and process disaster data
def fetch_and_process_data():
    disaster_data = solara_app.fetch_disaster_data()
    # Process the data as needed, e.g., extract latitude and longitude
    # For demonstration purposes, let's assume the data has 'latitude' and 'longitude' fields
    return disaster_data

# Route for rendering map view using Altair
@app.route('/map')
def map_view():
    disaster_data = fetch_and_process_data()
    
    # Convert disaster data to DataFrame for Altair
    df = pd.DataFrame(disaster_data)
    
    # Create Altair chart
    chart = alt.Chart(df).mark_circle().encode(
        latitude='latitude:Q',
        longitude='longitude:Q',
        tooltip=['name', 'description']
    ).properties(
        width=800,
        height=600
    )
    
    return render_template('map_view.html', chart=chart.to_json())

# Route for rendering other visualizations
@app.route('/other_visualization')
def other_visualization():
    # Add code to render other types of visualizations
    return render_template('other_visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
