from faker import Faker
from datetime import datetime


fake = Faker()


def get_first_name() -> str:
    """
    Generate first name by
    taking the first half of the full name
    """
    return fake.name().split(' ')[0]

def get_last_name() -> str:
    """
    Generate last name by
    taking the last half of the full name
    """
    return fake.name().split(' ')[1]

def get_address() -> str:
    """
    Generate address by
    formatting the address in one line
    """
    return fake.address().replace('\n', ' ')

def get_dob() -> str:
    """
    Generate datetime in dd/mm/yyyy format
    """
    return datetime.strftime(fake.date_time_this_decade(), "%d/%m/%Y")

def generate_customer_data() -> list:
    """
    Generate the first, last names, address and dob data 
    """
    return [
        get_first_name(),
        get_last_name(),
        get_address(),
        get_dob()
    ]
