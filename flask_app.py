from flask import Flask, render_template
import altair as alt
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Function to fetch and process disaster data from CSV
def fetch_and_process_data():
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv('disaster_data.csv')
        print("CSV data loaded successfully.")
        return df
    except FileNotFoundError:
        print("Error: disaster_data.csv not found.")
        return pd.DataFrame(columns=['name', 'description', 'total_affected', 'total_injured', 'total_missing', 'total_killed', 'total_displaced', 'economic_impact'])

# Route for rendering bar chart view using Altair
@app.route('/chart')
def chart_view():
    print("chart_view route accessed.")
    disaster_data = fetch_and_process_data()
    
    if disaster_data.empty:
        return "No data available or error loading data.", 500
    
    # Create Altair chart
    chart = alt.Chart(disaster_data).mark_bar().encode(
        x='name:N',
        y='total_affected:Q',
        tooltip=['name', 'description', 'total_affected', 'total_injured', 'total_missing', 'total_killed', 'total_displaced', 'economic_impact']
    ).properties(
        width=800,
        height=600
    )
    
    return render_template('chart_view.html', chart=chart.to_json())

if __name__ == '__main__':
    app.run(debug=True)
