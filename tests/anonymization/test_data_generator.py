from anonymization.data_generator import generate_customer_data


def test_get_customer_data(mocker):
    mocker.patch('anonymization.data_generator.get_first_name', return_value='firstname')
    mocker.patch('anonymization.data_generator.get_last_name', return_value='lastname')
    mocker.patch('anonymization.data_generator.get_address', return_value='address')
    mocker.patch('anonymization.data_generator.get_dob', return_value='04/03/1988')

    expected = [
        'firstname',
        'lastname',
        'address',
        '04/03/1988'
    ]

    result = generate_customer_data()

    assert result == expected
