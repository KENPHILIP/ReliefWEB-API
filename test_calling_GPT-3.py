from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import openai
import pandas as pd
import os

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model_path = 'random_forest_model.joblib'
data_path = 'processed_disasters_data.csv'

if not os.path.exists(model_path):
    raise HTTPException(status_code=404, detail="Model file not found.")

if not os.path.exists(data_path):
    raise HTTPException(status_code=404, detail="Data file not found.")

model = joblib.load(model_path)
df = pd.read_csv(data_path)

# Define a request body schema
class DisasterRequest(BaseModel):
    country: str
    year: int
    day: int

class QueryRequest(BaseModel):
    query: str

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise HTTPException(status_code=400, detail="OpenAI API key not found. Set it as an environment variable.")

# Define the prediction endpoint
@app.post("/predict")
def predict_disaster(request: DisasterRequest):
    try:
        # Validate input data
        if request.country not in df['country'].unique():
            raise HTTPException(status_code=400, detail="Invalid country.")

        if request.year < df['year'].min() or request.year > df['year'].max():
            raise HTTPException(status_code=400, detail="Invalid year.")

        if request.day < 1 or request.day > 31:
            raise HTTPException(status_code=400, detail="Invalid day.")

        # Create a DataFrame from the request data
        input_data = pd.DataFrame([{
            'year': request.year,
            'day': request.day,
            'country_' + request.country: 1  # One-hot encode the country
        }])

        # Ensure all country columns are present
        for col in model.feature_names_in_:
            if col not in input_data.columns:
                input_data[col] = 0

        # Make a prediction
        prediction = model.predict(input_data)
        return {"prediction": int(prediction[0] + 1)}  # Adjust back to month 1-12
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define the query endpoint for LLM
@app.post("/query")
def query_disaster(request: QueryRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=request.query,
            max_tokens=100
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
