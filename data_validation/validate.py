from datetime import datetime


def validate_transaction_data(data):
    """
    Function to validate data from stream to check if it matches requirement of SQL table
    :param data: data from stream to be validated
    :return: errors: python list of errors encountered
    """
    errors = []

    for index, row in data.iterrows():
        if not isinstance(row['transaction_id'], str):
            errors.append(f'Row {index}, transaction_id must be a string.')

        if not isinstance(row['user_id'], str):
            errors.append(f'Row {index}, user_id must be a string.')

        if not isinstance(row['product'], str):
            errors.append(f'Row {index}, product must be a string.')

        if row['quantity'] <= 0:
            errors.append(f'Row {index}, quantity must be greater than 0.')

        if row['price'] <= 0:
            errors.append(f'Row {index},  price must be greater than 0.')

        try:
            datetime.fromisoformat(row['timestamp'])
        except ValueError:
            errors.append(f'Row {index},  timestamp value is not a valid date time format.')

    return errors
