from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import CustomerInput
import pandas as pd
from model.predict import predict_output, MODEL_VERSION, model



app = FastAPI() 




# ✅ Prediction API
@app.post("/predict")
def predict_churn(data: CustomerInput):

    try:
        # Convert Pydantic model → dict
        input_dict = data.model_dump()

        # Pass dict directly
        prediction, probability = predict_output(input_dict)

        return JSONResponse(
            status_code=200,
            content={
                "churn": int(prediction),
                "probability": round(float(probability), 3),
                "result": "Customer will churn ❌" if prediction == 1 else "Customer will stay ✅"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

   

# ✅ Health Check Endpoint By Humans
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running 🚀"}


#Health Check By Machine
@app.get('/health')
def health_check():
    return {
        "status" : "OK",
        "version" : MODEL_VERSION,
        "model_loaded": model is not None
    }