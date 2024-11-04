import pandas as pd
import psycopg2
from kafka import KafkaConsumer
import json
from data_validation.validate import validate_transaction_data

# Connect to PostgresSQL
conn = psycopg2.connect(
    dbname="synthetic_data",
    user="postgres",
    password="qwertyuiop",
    host="localhost"
)
cursor = conn.cursor()

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumer-group'
)
for message in consumer:
    # Assume the message is a dictionary with keys matching the database columns
    data = json.loads(message.value.decode('utf-8'))

    # Create dataframe for consumed data
    transaction_data = pd.DataFrame([data])

    # Check for validation errors in consumed data
    validation_errors = validate_transaction_data(transaction_data)

    # Print all validation errors if any
    if validation_errors:
        for error in validation_errors:
            print(error)
    # Insert to table if no validation error
    else:
        cursor.execute(
            """
            INSERT INTO transactions (transaction_id, user_id, product, quantity, price, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (data["transaction_id"], data["user_id"], data["product"], data["quantity"], data["price"],
             data["timestamp"])
        )
    conn.commit()

# Close connection
cursor.close()
conn.close()
