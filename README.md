Pharma Intelligence Engine

This is a simple Machine Learning + FastAPI project that predicts drug categories based on drug information like name, class, and therapeutic group.

What this project does

Input :
- Active ingredient
- Pharmacological class
- Therapeutic group
- Brand name

And it predicts the disease category like:
- Cardiovascular
- Endocrine
- Neurological
- Gastrointestinal

It also saves all predictions automatically in a CSV file.

---

## ⚙️ How it works : Input → Text combine → TF-IDF → Logistic Regression → Prediction → Save CSV


Model used

- Logistic Regression
- TF-IDF Vectorizer

Why this model:
- Fast and simple
- Works well for text data
- Good for API deployment
- Lightweight and stable

Project structure
src/
├── api/
│   └── api.py
├── models/
│   ├── train.py
│   └── predict.py
├── preprocessing/
│   └── regex_extractor.py
├── utils/
│   └── io.py
outputs/
├── model.pkl
└── predictions.csv



🌐 API details
Endpoint
POST /predict
Input
{  "active_ingredient": "Metformin",  "pharmacological_class": "Biguanide",  "therapeutic_group": "Antidiabetic",  "brand_name": "Glucophage"}
Output
{  "prediction": "Endocrine"}

💾 Output
All predictions are saved in:
outputs/predictions.csv
