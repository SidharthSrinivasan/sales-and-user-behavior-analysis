-- Total Sales

SELECT SUM(quantity*price) AS total_sales_in_$ FROM transactions;


-- Total Sales by Day

SELECT date_trunc('day', timestamp) AS day, SUM(price*quantity) AS day_sales
FROM transactions
GROUP BY day
ORDER BY day;


-- Average Transaction Value

SELECT AVG(price*quantity) AS average_transaction_value FROM transactions;