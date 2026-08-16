import pandas as pd
import sqlite3
import os

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned/banking_transactions_cleaned.csv"
)

# Create database folder
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

database_folder = os.path.join(
    project_root,
    "sql"
)

os.makedirs(
    database_folder,
    exist_ok=True
)

# Database path
database_path = os.path.join(
    database_folder,
    "banking_analytics.db"
)

# Connect to SQLite database
connection = sqlite3.connect(database_path)

# Load DataFrame into SQL table
df.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("===================================")
print("SQL DATABASE CREATED SUCCESSFULLY!")
print("===================================")
print(f"Database: {database_path}")
print("Table: transactions")
print(f"Rows loaded: {len(df)}")