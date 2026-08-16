import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned/banking_transactions_cleaned.csv"
)

# Convert date
df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"]
)

print("=" * 50)
print("BANKING CUSTOMER TRANSACTION ANALYSIS")
print("=" * 50)

# --------------------------------------------------
# 1. Basic statistics
# --------------------------------------------------

print("\n========== BASIC STATISTICS ==========")

print("Total Customers:",
      df["Customer_ID"].nunique())

print("Total Transactions:",
      df["Transaction_ID"].nunique())

print("Total Transaction Amount:",
      round(df["Amount"].sum(), 2))

print("Average Transaction Amount:",
      round(df["Amount"].mean(), 2))

print("Maximum Transaction Amount:",
      round(df["Amount"].max(), 2))

print("Minimum Transaction Amount:",
      round(df["Amount"].min(), 2))


# --------------------------------------------------
# 2. Transaction Type Analysis
# --------------------------------------------------

print("\n========== TRANSACTION TYPE ==========")

transaction_type = (
    df.groupby("Transaction_Type")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum"),
          Average_Amount=("Amount", "mean")
      )
      .sort_values(
          by="Total_Amount",
          ascending=False
      )
)

print(transaction_type.round(2))


# --------------------------------------------------
# 3. Payment Method Analysis
# --------------------------------------------------

print("\n========== PAYMENT METHOD ==========")

payment_analysis = (
    df.groupby("Payment_Method")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum")
      )
      .sort_values(
          by="Transactions",
          ascending=False
      )
)

print(payment_analysis.round(2))


# --------------------------------------------------
# 4. City Analysis
# --------------------------------------------------

print("\n========== CITY ANALYSIS ==========")

city_analysis = (
    df.groupby("City")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum"),
          Average_Amount=("Amount", "mean")
      )
      .sort_values(
          by="Total_Amount",
          ascending=False
      )
)

print(city_analysis.round(2))


# --------------------------------------------------
# 5. Account Type Analysis
# --------------------------------------------------

print("\n========== ACCOUNT TYPE ==========")

account_analysis = (
    df.groupby("Account_Type")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum"),
          Average_Amount=("Amount", "mean")
      )
      .sort_values(
          by="Total_Amount",
          ascending=False
      )
)

print(account_analysis.round(2))


# --------------------------------------------------
# 6. Gender Analysis
# --------------------------------------------------

print("\n========== GENDER ANALYSIS ==========")

gender_analysis = (
    df.groupby("Gender")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum"),
          Average_Amount=("Amount", "mean")
      )
)

print(gender_analysis.round(2))


# --------------------------------------------------
# 7. Monthly Analysis
# --------------------------------------------------

print("\n========== MONTHLY ANALYSIS ==========")

df["Month"] = df["Transaction_Date"].dt.to_period("M")

monthly_analysis = (
    df.groupby("Month")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum")
      )
)

print(monthly_analysis.round(2))


# --------------------------------------------------
# 8. Top 10 Customers
# --------------------------------------------------

print("\n========== TOP 10 CUSTOMERS ==========")

top_customers = (
    df.groupby("Customer_ID")
      .agg(
          Transactions=("Transaction_ID", "count"),
          Total_Amount=("Amount", "sum")
      )
      .sort_values(
          by="Total_Amount",
          ascending=False
      )
      .head(10)
)

print(top_customers.round(2))