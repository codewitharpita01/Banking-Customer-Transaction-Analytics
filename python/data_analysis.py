import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/banking_transactions.csv")

# Display first 5 rows
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Dataset information
print("\n========== DATASET INFO ==========")
print(df.info())

# Statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())