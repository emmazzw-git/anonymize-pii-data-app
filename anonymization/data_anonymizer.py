from typing import Iterable, Iterator, Callable
from anonymization.data_generator import (
    get_first_name,
    get_last_name,
    get_address
)


FIRST_NAME_COLUMN = 'first_name'
LAST_NAME_COLUMN = 'last_name'
ADDRESS_COLUMN = 'address'


def anonymize_customer_data(rows: Iterable[str]) -> Iterator[str]:
    """
    Anonymize first_name, last_name and address by
    replacing their values with fake values
    """
    for row in rows:
        row[FIRST_NAME_COLUMN] = generate_unidentical_value(
            row[FIRST_NAME_COLUMN],
            get_first_name
        )
        row[LAST_NAME_COLUMN] = generate_unidentical_value(
            row[LAST_NAME_COLUMN],
            get_last_name
        )
        row[ADDRESS_COLUMN] = generate_unidentical_value(
            row[ADDRESS_COLUMN],
            get_address
        )

        yield row

def generate_unidentical_value(real_value: str, get_fn: Callable) -> str:
    """
    Generate a different first name than the real firstname
    """
    new_value = get_fn()
    while new_value == real_value:
        new_value = get_fn()
    
    return new_value