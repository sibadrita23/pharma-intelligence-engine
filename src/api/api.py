from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib

# =========================
# LOAD MODEL
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "outputs" / "model.pkl"

bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
label_encoder = bundle["label_encoder"]

# =========================
# APP
# =========================
app = FastAPI(
    title="Pharma Intelligence API",
    version="1.0"
)

# =========================
# INPUT SCHEMA
# =========================
class DrugInput(BaseModel):
    active_ingredient: str
    pharmacological_class: str
    therapeutic_group: str
    brand_name: str

# =========================
# PREDICT FUNCTION
# =========================
def predict_label(data: DrugInput):
    text = f"{data.active_ingredient} {data.pharmacological_class} {data.therapeutic_group} {data.brand_name}"
    pred = model.predict([text])[0]
    return label_encoder.inverse_transform([pred])[0]

# =========================
# ROUTES
# =========================
@app.get("/")
def home():
    return {"status": "Pharma API running"}

@app.post("/predict")
def predict(data: DrugInput):
    return {
        "input": data.dict(),
        "prediction": predict_label(data)
    }