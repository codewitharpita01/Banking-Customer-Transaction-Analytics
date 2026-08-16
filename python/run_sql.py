import sqlite3
import os

# Project root
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Database path
database_path = os.path.join(
    project_root,
    "sql",
    "banking_analytics.db"
)

# Connect to database
connection = sqlite3.connect(database_path)

cursor = connection.cursor()

print("=" * 60)
print("BANKING SQL ANALYSIS")
print("=" * 60)


# --------------------------------------------------
# 1. Total Transactions
# --------------------------------------------------

cursor.execute("""
SELECT COUNT(*)
FROM transactions
""")

result = cursor.fetchone()

print("\n1. TOTAL TRANSACTIONS")
print(result[0])


# --------------------------------------------------
# 2. Total Transaction Amount
# --------------------------------------------------

cursor.execute("""
SELECT ROUND(SUM(Amount), 2)
FROM transactions
""")

result = cursor.fetchone()

print("\n2. TOTAL TRANSACTION AMOUNT")
print(result[0])


# --------------------------------------------------
# 3. Average Transaction Amount
# --------------------------------------------------

cursor.execute("""
SELECT ROUND(AVG(Amount), 2)
FROM transactions
""")

result = cursor.fetchone()

print("\n3. AVERAGE TRANSACTION AMOUNT")
print(result[0])


# --------------------------------------------------
# 4. Transaction Type Analysis
# --------------------------------------------------

print("\n4. TRANSACTION TYPE ANALYSIS")

cursor.execute("""
SELECT
    Transaction_Type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount,
    ROUND(AVG(Amount), 2) AS average_amount
FROM transactions
GROUP BY Transaction_Type
ORDER BY total_amount DESC
""")

for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 5. Payment Method Analysis
# --------------------------------------------------

print("\n5. PAYMENT METHOD ANALYSIS")

cursor.execute("""
SELECT
    Payment_Method,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY Payment_Method
ORDER BY transaction_count DESC
""")

for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 6. City Analysis
# --------------------------------------------------

print("\n6. CITY ANALYSIS")

cursor.execute("""
SELECT
    City,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY City
ORDER BY total_amount DESC
""")

for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 7. Account Type Analysis
# --------------------------------------------------

print("\n7. ACCOUNT TYPE ANALYSIS")

cursor.execute("""
SELECT
    Account_Type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY Account_Type
ORDER BY total_amount DESC
""")

for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 8. Top 10 Customers
# --------------------------------------------------

print("\n8. TOP 10 CUSTOMERS")

cursor.execute("""
SELECT
    Customer_ID,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY Customer_ID
ORDER BY total_amount DESC
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 9. Monthly Analysis
# --------------------------------------------------

print("\n9. MONTHLY ANALYSIS")

cursor.execute("""
SELECT
    strftime('%Y-%m', Transaction_Date) AS month,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY month
ORDER BY month
""")

for row in cursor.fetchall():
    print(row)


# Close database
connection.close()

print("\n" + "=" * 60)
print("SQL ANALYSIS COMPLETED!")
print("=" * 60)