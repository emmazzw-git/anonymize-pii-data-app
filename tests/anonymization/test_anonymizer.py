from unittest.mock import Mock
from anonymization.data_anonymizer import (
    generate_unidentical_value
)


def test_generate_unidentical_value():
    mock_get_fn = Mock()
    mock_get_fn.side_effect = ['firstname1', 'firstname1', 'firstname3']

    anonymized_firstname = generate_unidentical_value('firstname1', mock_get_fn)
    expected_firstname = 'firstname3'

    assert anonymized_firstname == expected_firstname

