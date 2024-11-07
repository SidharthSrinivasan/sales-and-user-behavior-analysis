-- Peak transaction times

SELECT EXTRACT(HOUR FROM timestamp) AS hour, COUNT(*) AS transactions_count
FROM transactions
GROUP BY hour
ORDER BY transactions_count DESC;

-- Average quantity per transaction:

SELECT AVG(quantity) AS avg_quantity_per_transaction
FROM transactions;