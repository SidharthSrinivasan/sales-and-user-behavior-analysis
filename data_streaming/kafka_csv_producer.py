from kafka import KafkaProducer
import time
import json
import pandas as pd


def produce_data_from_csv(csv_file):
    """
    Function to load transaction data and use Kafka Producer to stream the data
    :param csv_file: The synthetic transaction data csv file
    :return:
    """

    # Load the synthetic transaction data
    transaction_df = pd.read_csv(csv_file)

    # Initialize Kafka producer
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Stream each transaction record
    for index, row in transaction_df.iterrows():
        producer.send('transactions', value=row.to_dict())
        print(f'Sent: {row.to_dict()}')  # Print the sent record for verification
        time.sleep(0.1)  # Sleep to simulate streaming

    producer.flush()
    producer.close()


if __name__ == '__main__':
    try:
        produce_data_from_csv('../data_generation/synthetic_transaction_data.csv')  # Specify CSV path here
    except Exception as e:
        print(f"An Error Occurred {e}")
