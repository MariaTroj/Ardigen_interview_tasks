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


@pytest.mark.parametrize("file_path, exception_type", [
    ('test1.csv', TypeError),
])
def test_csv_data_to_dict(file_path, exception_type):
    with pytest.raises(exception_type) as e:
        data = CSVReader.read_csv(file_path)
        output = CSVReader.csv_data_to_dict(data)
    assert e is not None


@pytest.mark.parametrize("file_path", [
    'test_output.csv',
])
def test_write_csv(file_path):
    data = [{'ticket': '20min', 'price': '2.0', 'type': 'discount'}]
    CSVReader.write_csv(file_path, data)
    output = CSVReader.read_csv(file_path)
    assert output == data


@pytest.mark.parametrize("file_path, exception_type", [
    ('test_output.csv', ValueError),
])
def test_try_to_write(file_path, exception_type):
    data = {'ticket': '20min', 'price': '2.0', 'type': 'discount'}
    with pytest.raises(exception_type) as e:
        CSVReader.write_csv(file_path, data)
    assert e is not None


