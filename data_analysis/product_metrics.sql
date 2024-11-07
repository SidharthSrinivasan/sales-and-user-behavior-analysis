-- Top 10 Products Sold

SELECT product, SUM(quantity) as quantity_sold
FROM transactions
GROUP BY product
ORDER BY quantity_sold DESC
LIMIT 10;

-- Top 10 Products with Highest Revenue

SELECT product, SUM(price*quantity) AS sales
FROM transactions
GROUP BY product
ORDER BY sales DESC
LIMIT 10;

-- Month when most products were sold

SELECT date_trunc('month', timestamp) AS month, SUM(quantity) AS products_sold
FROM transactions
GROUP BY month
ORDER BY products_sold DESC
LIMIT 1;

-- Total quantity of each product sold each month
SELECT date_trunc('month', timestamp) AS month, SUM(quantity) AS products_sold, product
FROM transactions
GROUP BY month, product

-- Most sold product in each month
SELECT month, product, products_sold
FROM (
    SELECT date_trunc('month', timestamp) AS month, product, SUM(quantity) AS products_sold,
    RANK() OVER (PARTITION BY date_trunc('month', timestamp) ORDER BY SUM(quantity) DESC) AS rank
    FROM transactions
    GROUP BY month, product
) AS ranked_products
WHERE rank = 1;
