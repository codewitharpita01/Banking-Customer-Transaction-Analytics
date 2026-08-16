import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned/banking_transactions_cleaned.csv"
)

# Convert date
df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"]
)

# Create visualizations folder automatically
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

visualization_folder = os.path.join(
    project_root,
    "visualizations"
)

os.makedirs(
    visualization_folder,
    exist_ok=True
)

# ==================================================
# 1. Transaction Type Distribution
# ==================================================

transaction_counts = df["Transaction_Type"].value_counts()

plt.figure(figsize=(8, 5))

transaction_counts.plot(kind="bar")

plt.title("Transaction Type Distribution")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "transaction_type_distribution.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 2. Payment Method Distribution
# ==================================================

payment_counts = df["Payment_Method"].value_counts()

plt.figure(figsize=(8, 5))

payment_counts.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "payment_method_distribution.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 3. Monthly Transaction Trend
# ==================================================

df["Month"] = df["Transaction_Date"].dt.to_period("M")

monthly_transactions = (
    df.groupby("Month")["Amount"]
      .sum()
)

plt.figure(figsize=(12, 5))

monthly_transactions.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Transaction Amount Trend")
plt.xlabel("Month")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "monthly_transaction_trend.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 4. City-wise Transaction Amount
# ==================================================

city_amount = (
    df.groupby("City")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

city_amount.plot(kind="bar")

plt.title("Total Transaction Amount by City")
plt.xlabel("City")
plt.ylabel("Transaction Amount")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "city_transaction_amount.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 5. Account Type Analysis
# ==================================================

account_amount = (
    df.groupby("Account_Type")["Amount"]
      .sum()
)

plt.figure(figsize=(7, 5))

account_amount.plot(
    kind="bar"
)

plt.title("Transaction Amount by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "account_type_analysis.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 6. Transaction Amount Distribution
# ==================================================

plt.figure(figsize=(9, 5))

sns.histplot(
    df["Amount"],
    bins=50,
    kde=True
)

plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "transaction_amount_distribution.png"
    )
)

plt.show()
plt.close()


# ==================================================
# 7. Correlation Heatmap
# ==================================================

numeric_columns = [
    "Age",
    "Amount",
    "Balance"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    os.path.join(
        visualization_folder,
        "correlation_heatmap.png"
    )
)

plt.show()
plt.close()


print("\n====================================")
print("ALL VISUALIZATIONS CREATED!")
print("====================================")

print("\nFiles saved in:")
print("visualizations/")