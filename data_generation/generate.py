from faker import Faker
import pandas as pd

fake = Faker()


# Generate synthetic user data
def generate_user_data(num_data):
    """
    Function to generate random synthetic user data

    :param num_data: The number of records of user data to be created
    :return: pd.DataFrame: A dataframe consisting of the generated synthetic user data
    """
    user_data = []
    for i in range(num_data):
        user_data.append({
            "user_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "sign_up_date": fake.date_this_decade(),
            "location": fake.city()
        })
    return pd.DataFrame(user_data)


def generate_transaction_data(num_data, user_ids):
    """
    Function to generate random synthetic transaction data

    :param num_data: The number of records of transaction data to be created
    :param user_ids: user ids to be used to generate transaction data
    :return: pd.Dataframe: A dataframe consisting of all generated synthetic transaction data
    """
    transaction_data = []
    for i in range(num_data):
        transaction_data.append({
            "transaction_id": fake.uuid4(),
            "user_id": fake.random_element(user_ids),  # To indicate which user has purchased
            "product": fake.word(),
            "quantity": fake.random_int(min=1, max=5),
            "price": round(fake.random_number(digits=3), 2),
            "timestamp": fake.date_time_this_year()
        })
    return pd.DataFrame(transaction_data)


# Generate and save 1000 records of user data
user_df = generate_user_data(1000)
print(user_df.head())
user_df.to_csv('synthetic_user_data.csv')


# Generate and save 5000 records of transaction data
transaction_df = generate_transaction_data(5000, user_df["user_id"].tolist())
print(transaction_df.head())
transaction_df.to_csv('synthetic_transaction_data.csv')