import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from preprocessing.regex_extractor import extract_fields

file_path = os.path.join(os.path.dirname(__file__), "../data/pharma_messages.csv")
df = pd.read_csv(file_path)


samples = df["message"].head(5)

for i, sample in enumerate(samples):
    print(f"\n===== SAMPLE {i+1} =====\n")
    
    extracted = extract_fields(sample)
    
    for k, v in extracted.items():
        print(f"{k}: {v}")

print("\nEXTRACTED:\n", extract_fields(sample))