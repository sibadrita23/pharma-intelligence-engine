import re

def extract_fields(text):
    patterns = {
        "disease": r"Disease:\s*(.*)",
        "indication": r"Indication:\s*(.*?)\s*\(",
        "category": r"Category:\s*(.*?)\)",
        "drug": r"Drug:\s*(.*?)\s*\(",
        "brand": r"Brand:\s*(.*?)\)",
        "pharmacological_class": r"Pharmacological Class:\s*(.*)",
        "drug_type": r"Drug Type:\s*(.*)",
        "strength": r"Strength:\s*(.*)",
        "dosage_form": r"Dosage Form:\s*(.*)",
        "route": r"Route:\s*(.*)",
        "side_effects": r"Side Effects:\s*(.*)",
        "pregnancy_category": r"Pregnancy Category:\s*(.*)",
        "prescription_type": r"Prescription Type:\s*(.*)"
    }

    data = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        data[key] = match.group(1).strip() if match else None

    return data