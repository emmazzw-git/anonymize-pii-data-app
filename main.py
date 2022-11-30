
import csv
from anonymization.data_generator import generate_customer_data
from anonymization.data_anonymizer import anonymize_customer_data

FIRST_NAME_COLUMN = 'first_name'
LAST_NAME_COLUMN = 'last_name'
ADDRESS_COLUMN = 'address'
DOB_COLUMN = 'date_of_birth'

SOURCE_FILE = '/output/customer_data.csv'
TARGET_FILE = '/output/anonymized_data.csv'

# Step 1: generate customer data and write to csv file
def data_generate(target) -> None:
    """
    Generate customer data and write to the csv file
    """
    with open(target, 'w') as o:
        writer = csv.writer(o)
        writer.writerow([
            FIRST_NAME_COLUMN,
            LAST_NAME_COLUMN,
            ADDRESS_COLUMN,
            DOB_COLUMN
        ])

        for n in range(1, 10):
            writer.writerow((generate_customer_data()))


# Step 2: anonymize the first, last names and address data and write to csv file
def anonymize(source, target) -> None:
    """
    Anonymize customer data and write to the csv file
    """
    with open(source, 'r') as f:
        with open(target, 'w') as o:
            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)
            writer.writeheader()

            for row in anonymize_customer_data(reader):
                writer.writerow(row)


if __name__ == '__main__':
    data_generate(
        SOURCE_FILE
    )

    anonymize(
        SOURCE_FILE,
        TARGET_FILE
    )