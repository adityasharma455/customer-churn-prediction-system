import pandas as pd
import joblib
from fastapi.responses import JSONResponse



# Load saved files
model = joblib.load("model/churn_model.pkl")
#I create it manually but it come form ml flow software
MODEL_VERSION = '1.0.0'

scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/columns.pkl")

def predict_output(user_input: dict):
        
            
        # Convert dict to DataFrame
        input_df = pd.DataFrame([user_input])

   
         # One-hot encoding (same as training)
        input_df = pd.get_dummies(user_input)

        # Align with training columns
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Predict
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        return prediction, probability
    
   