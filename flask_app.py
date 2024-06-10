from flask import Flask, render_template
import solara_app

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    try:
        disaster_data = solara_app.fetch_disaster_data()
    except Exception as e:
        disaster_data = []
        print(f"Error fetching disaster data: {e}")

    return render_template('index.html', disasters=disaster_data)

if __name__ == '__main__':
    app.run(debug=True)
