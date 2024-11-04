
import psycopg2
from kafka import KafkaConsumer
import json

# Connect to PostgreSQL
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

    cursor.execute(
        """
        INSERT INTO transactions (transaction_id, user_id, product, quantity, price, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (data["transaction_id"], data["user_id"], data["product"], data["quantity"], data["price"], data["timestamp"])
    )
    conn.commit()

# Close connection
cursor.close()
conn.close()
