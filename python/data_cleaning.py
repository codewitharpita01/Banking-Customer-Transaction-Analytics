import pandas as pd
import os

# Load raw dataset
df = pd.read_csv("data/raw/banking_transactions.csv")

print("========== ORIGINAL DATA ==========")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# --------------------------------------------------
# 1. Convert Transaction_Date to datetime
# --------------------------------------------------

df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"]
)

# --------------------------------------------------
# 2. Check missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# --------------------------------------------------
# 3. Remove duplicate records
# --------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate records found: {duplicates}")

df = df.drop_duplicates()

# --------------------------------------------------
# 4. Check invalid values
# --------------------------------------------------

print("\n========== INVALID VALUES ==========")

print("Invalid Age:",
      ((df["Age"] < 18) | (df["Age"] > 100)).sum())

print("Invalid Amount:",
      (df["Amount"] <= 0).sum())

print("Invalid Balance:",
      (df["Balance"] < 0).sum())

# --------------------------------------------------
# 5. Fix invalid Age
# --------------------------------------------------

df = df[
    (df["Age"] >= 18) &
    (df["Age"] <= 100)
]

# --------------------------------------------------
# 6. Fix invalid Amount
# --------------------------------------------------

df = df[df["Amount"] > 0]

# --------------------------------------------------
# 7. Fix invalid Balance
# --------------------------------------------------

df = df[df["Balance"] >= 0]

# --------------------------------------------------
# 8. Sort by transaction date
# --------------------------------------------------

df = df.sort_values(
    by="Transaction_Date"
)

# --------------------------------------------------
# 9. Reset index
# --------------------------------------------------

df = df.reset_index(drop=True)

# --------------------------------------------------
# 10. Save cleaned dataset
# --------------------------------------------------

# Create cleaned folder automatically
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

cleaned_folder = os.path.join(
    project_root,
    "data",
    "cleaned"
)

os.makedirs(cleaned_folder, exist_ok=True)

# Save cleaned dataset
output_path = os.path.join(
    cleaned_folder,
    "banking_transactions_cleaned.csv"
)

df.to_csv(
    output_path,
    index=False
)

# --------------------------------------------------
# Final information
# --------------------------------------------------

print("\n========== CLEANING COMPLETE ==========")
print(f"Final rows: {df.shape[0]}")
print(f"Final columns: {df.shape[1]}")

print("\nCleaned dataset saved successfully!")