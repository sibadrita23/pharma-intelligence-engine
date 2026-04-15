import pandas as pd
from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "pharma_messages.csv"
MODEL_PATH = BASE_DIR / "outputs" / "model.pkl"

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# TARGET
# =========================
y = df["indication_category"]

# encode labels (important for stability)
le = LabelEncoder()
y = le.fit_transform(y)

# =========================
# FEATURES (IMPORTANT FIX)
# Combine meaningful text fields
# =========================
df["text"] = (
    df["active_ingredient"].astype(str) + " " +
    df["pharmacological_class"].astype(str) + " " +
    df["therapeutic_group"].astype(str) + " " +
    df["brand_name"].astype(str)
)

X = df[["text"]]

# =========================
# MODEL PIPELINE
# =========================
model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", LogisticRegression(max_iter=2000, class_weight="balanced"))
])

# =========================
# TRAIN / TEST
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X["text"], y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print("Model Accuracy:", round(acc, 3))

# =========================
# SAVE MODEL + LABELS
# =========================
joblib.dump({
    "model": model,
    "label_encoder": le
}, MODEL_PATH)

print("Model saved at:", MODEL_PATH)