import pandas as pd
import os


file_path = os.path.join(os.path.dirname(__file__), "C:\\Users\\SHIBADRITA\\Downloads\\pharma_realistic_10000.csv")

df = pd.read_csv(file_path)


def create_message(row):
    message = f"""
Disease: {row['indication']}

→ Indication: {row['indication']} (Category: {row['indication_category']})

→ Drug: {row['active_ingredient']} (Brand: {row['brand_name']})
→ Pharmacological Class: {row['pharmacological_class']}
→ Drug Type: {row['drug_type']}
→ Strength: {row['strength']}
→ Dosage Form: {row['dosage_form']}
→ Route: {row['route']}

→ Safety & Usage:
   • Side Effects: {row['side_effects']}
   • Pregnancy Category: {row['pregnancy_category']}
   • Controlled Substance: {"Yes" if row['controlled_substance'] == 1 else "No"}
   • Prescription Type: {row['otc_or_rx']}
   • Food Interaction: {"Yes" if row['food_interaction'] == 1 else "No"}
   • Alcohol Interaction: {"Yes" if row['alcohol_interaction'] == 1 else "No"}

→ Composition:
   • Number of Ingredients: {row['num_ingredients']}
   • Combination Drug: {"Yes" if row['is_combination_drug'] == 1 else "No"}
"""
    return message



df["message"] = df.apply(create_message, axis=1)


print("\n===== SAMPLE MESSAGE =====\n")
print(df["message"].iloc[0])


def search_by_indication(query):
    result = df[
        df["indication"].str.contains(query, case=False, na=False) |
        df["indication_category"].str.contains(query, case=False, na=False)
    ]
    
    if result.empty:
        print("\n❌ No results found")
    else:
        print(f"\n✅ Found {len(result)} results\n")
        for msg in result["message"].head(3):
            print(msg)
            print("-" * 50)
            

# Test search
search_by_indication("Cardiovascular disease prevention")
search_by_indication("respiratory")
search_by_indication("diabetes")
search_by_indication("infection")

