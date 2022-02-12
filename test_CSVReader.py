from ValuationService import CSVReader
import pytest


@pytest.mark.parametrize("file_path, expected_output", [
    ('test.csv', [{'ticket': '20min', 'price': '4.0'}, {'ticket': '60min', 'price': '6.0'}]),
])
def test_read_csv(file_path, expected_output):
    output = CSVReader.read_csv(file_path)
    assert output == expected_output


@pytest.mark.parametrize("file_path, expected_output", [
    ('test.csv', {'20min' : '4.0', '60min' : '6.0'}),
])
def test_csv_data_to_dict(file_path, expected_output):
    data = CSVReader.read_csv(file_path)
    output = CSVReader.csv_data_to_dict(data)
    assert output == expected_output


@pytest.mark.parametrize("file_path, exception_statement", [
    ('test1.csv', 'wrong data format: too many keys to wrap list into dict'),
])
def test_csv_data_to_dict(file_path, exception_statement):
    with pytest.raises(TypeError) as e:
        data = CSVReader.read_csv(file_path)
        output = CSVReader.csv_data_to_dict(data)
    assert e.value.args[0] == exception_statement


@pytest.mark.parametrize("file_path", [
    'test_output.csv',
])
def test_write_csv(file_path):
    data = [{'ticket': '20min', 'price': '2.0', 'type': 'discount'}]
    CSVReader.write_csv(file_path, data)
    output = CSVReader.read_csv(file_path)
    assert output == data


@pytest.mark.parametrize("file_path, exception_statement", [
    ('test_output.csv', 'wrong data format: list[dict] is expected'),
])
def test_try_to_write(file_path, exception_statement):
    data = {'ticket': '20min', 'price': '2.0', 'type': 'discount'}
    with pytest.raises(ValueError) as e:
        CSVReader.write_csv(file_path, data)
    assert e.value.args[0] == exception_statement


