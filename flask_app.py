from flask import Flask, render_template_string
import solara
from solara_app import create_disaster_dashboard

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    dashboard = create_disaster_dashboard()
    return solara.render(dashboard())

if __name__ == '__main__':
    app.run(debug=True)
