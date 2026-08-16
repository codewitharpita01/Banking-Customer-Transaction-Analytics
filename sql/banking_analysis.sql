-- ==========================================
-- BANKING CUSTOMER TRANSACTION ANALYTICS
-- ==========================================


-- 1. Total Transactions

SELECT
    COUNT(*) AS total_transactions
FROM transactions;


-- 2. Total Transaction Amount

SELECT
    ROUND(SUM(Amount), 2) AS total_transaction_amount
FROM transactions;


-- 3. Average Transaction Amount

SELECT
    ROUND(AVG(Amount), 2) AS average_transaction_amount
FROM transactions;


-- 4. Transaction Type Analysis

SELECT
    Transaction_Type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount,
    ROUND(AVG(Amount), 2) AS average_amount
FROM transactions
GROUP BY Transaction_Type
ORDER BY total_amount DESC;


-- 5. Payment Method Analysis

SELECT
    Payment_Method,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY Payment_Method
ORDER BY transaction_count DESC;


-- 6. City-wise Analysis

SELECT
    City,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount,
    ROUND(AVG(Amount), 2) AS average_amount
FROM transactions
GROUP BY City
ORDER BY total_amount DESC;


-- 7. Account Type Analysis

SELECT
    Account_Type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount,
    ROUND(AVG(Amount), 2) AS average_amount
FROM transactions
GROUP BY Account_Type
ORDER BY total_amount DESC;


-- 8. Top 10 Customers

SELECT
    Customer_ID,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY Customer_ID
ORDER BY total_amount DESC
LIMIT 10;


-- 9. Monthly Transaction Analysis

SELECT
    strftime('%Y-%m', Transaction_Date) AS month,
    COUNT(*) AS transaction_count,
    ROUND(SUM(Amount), 2) AS total_amount
FROM transactions
GROUP BY month
ORDER BY month;


-- 10. High Value Transactions

SELECT
    Transaction_ID,
    Customer_ID,
    Transaction_Date,
    Transaction_Type,
    Payment_Method,
    Amount
FROM transactions
WHERE Amount >= 90000
ORDER BY Amount DESC;