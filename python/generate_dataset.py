import pandas as pd
import numpy as np
import os

# Reproducible results
np.random.seed(42)

# Number of transactions
n = 10000

# Customer IDs
customer_ids = np.random.randint(1001, 2001, n)

# Transaction IDs
transaction_ids = [f"TXN{i:06d}" for i in range(1, n + 1)]

# Transaction dates
dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    periods=n
)

# Customer details
ages = np.random.randint(18, 71, n)

genders = np.random.choice(
    ["Male", "Female"],
    n
)

cities = np.random.choice(
    ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune"],
    n
)

account_types = np.random.choice(
    ["Savings", "Current"],
    n,
    p=[0.75, 0.25]
)

# Transaction details
transaction_types = np.random.choice(
    ["Deposit", "Withdrawal", "Transfer"],
    n,
    p=[0.35, 0.40, 0.25]
)

payment_methods = np.random.choice(
    ["UPI", "ATM", "Debit Card", "Net Banking"],
    n,
    p=[0.45, 0.20, 0.20, 0.15]
)

# Transaction amounts
amounts = np.round(
    np.random.uniform(100, 100000, n),
    2
)

# Account balance
balances = np.round(
    np.random.uniform(5000, 500000, n),
    2
)

# Create DataFrame
df = pd.DataFrame({
    "Transaction_ID": transaction_ids,
    "Customer_ID": customer_ids,
    "Transaction_Date": dates,
    "Age": ages,
    "Gender": genders,
    "City": cities,
    "Account_Type": account_types,
    "Transaction_Type": transaction_types,
    "Payment_Method": payment_methods,
    "Amount": amounts,
    "Balance": balances
})

# Get project root folder
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Create data/raw folder automatically
raw_folder = os.path.join(
    project_root,
    "data",
    "raw"
)

os.makedirs(raw_folder, exist_ok=True)

# Final CSV path
output_path = os.path.join(
    raw_folder,
    "banking_transactions.csv"
)

# Save dataset
df.to_csv(
    output_path,
    index=False
)

print("Dataset created successfully!")
print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"File saved at: {output_path}")

print("\nFirst 5 records:")
print(df.head())