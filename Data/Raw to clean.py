import pandas as pd
import numpy as np

# =========================
# 1. FILE PATH
# =========================
file_path = r"C:\Users\Shiva\Desktop\EMI Predict AI(FinTech)\Data\emi_prediction_dataset.csv"

print("\n[STEP 1] Loading dataset...")

# =========================
# 2. LOAD DATASET
# =========================
df = pd.read_csv(file_path, low_memory=False)

print("Dataset Loaded Successfully")
print("Initial Shape:", df.shape)

# =========================
# 3. BASIC INFO
# =========================
print("\n[STEP 2] Dataset Info")
print(df.info())

# =========================
# 4. REMOVE DUPLICATES
# =========================
duplicate_count = df.duplicated().sum()
print("\n[STEP 3] Duplicate Rows:", duplicate_count)

df = df.drop_duplicates()
print("Shape After Removing Duplicates:", df.shape)

# =========================
# 5. NUMERIC CLEANING
# =========================

integer_cols = ["age", "monthly_salary", "bank_balance"]
for col in integer_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
        
        # Remove repeating ".0" patterns at end
        df[col] = df[col].str.replace(r"(\.0)+$", "", regex=True)
        
        # Extract the main number
        df[col] = df[col].str.extract(r"(\d+)")[0]
        
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

# Columns where decimals are allowed
decimal_cols = [
    "years_of_employment","monthly_rent","family_size","dependents",
    "school_fees","college_fees","travel_expenses","groceries_utilities",
    "other_monthly_expenses","current_emi_amount","credit_score",
    "emergency_fund","requested_amount","requested_tenure","max_monthly_emi"
]

for col in decimal_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].str.extract(r"(\d+\.?\d*)")[0]
        df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================
# 6. CLEAN CATEGORICAL DATA
# =========================

# Normalize text columns
for col in ["gender","existing_loans"]:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Fix gender labels
df["gender"] = df["gender"].replace({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})

# Fix existing loans
df["existing_loans"] = df["existing_loans"].replace({
    "yes": "Yes",
    "y": "Yes",
    "no": "No",
    "n": "No"
})

# Convert categorical columns
categorical_cols = [
    "gender","marital_status","education","employment_type",
    "company_type","house_type","emi_scenario","emi_eligibility",
    "existing_loans"
]

for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype("category")

# =========================
# 7. MISSING VALUE REPORT AFTER CLEANING
# =========================
print("\n[STEP 4] Missing Value Report After Cleaning")
missing_report = df.isnull().sum().sort_values(ascending=False)
print(missing_report)

missing_report.to_csv("missing_value_report.csv")

# =========================
# 8. FINAL SHAPE
# =========================
print("\n[STEP 5] Final Dataset Shape:", df.shape)

# =========================
# 9. SAVE CLEANED DATA
# =========================
df.to_csv("cleaned_emi_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved as cleaned_emi_dataset.csv")
print("✅ Missing report saved as missing_value_report.csv")
