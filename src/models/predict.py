import joblib
from pathlib import Path

# =========================
# PATH
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "outputs" / "model.pkl"

# =========================
# LOAD MODEL
# =========================
bundle = joblib.load(MODEL_PATH)

model = bundle["model"]
label_encoder = bundle["label_encoder"]

print("Model loaded successfully!")

# =========================
# PREDICTION FUNCTION
# =========================
def predict_drug(active_ingredient, pharmacological_class, therapeutic_group, brand_name):
    text = f"{active_ingredient} {pharmacological_class} {therapeutic_group} {brand_name}"
    pred = model.predict([text])[0]
    return label_encoder.inverse_transform([pred])[0]

# =========================
# TEST CASES (FIXED OUTPUT)
# =========================
test_cases = [
    ("Metformin", "Biguanide", "Antidiabetic", "Glucophage"),
    ("Ibuprofen", "NSAID", "Analgesic", "Advil"),
    ("Insulin Glargine", "Insulin", "Antidiabetic", "Lantus"),
    ("Amoxicillin", "Beta-lactam", "Antibiotic", "Augmentin"),
    ("Atorvastatin", "Statin", "Lipid-lowering", "Atorin")
]

for i, t in enumerate(test_cases, 1):
    result = predict_drug(*t)
    print(f"\nCASE {i}")
    print("INPUT:", t)
    print("PREDICTION:", result)