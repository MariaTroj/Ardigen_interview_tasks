import pytest
from FizzBuzz import fizzbuzz


def test_fizzbuzz_has_input_argument():
    assert 'input' in fizzbuzz.__annotations__.keys()


def test_fizzbuzz_has_return_statement():
    assert 'return' in fizzbuzz.__annotations__.keys()


@pytest.mark.parametrize("corrrect_input, expected_output", [
    ("1\n2", '1\n2'),
    ("1\n3", '1\n2\nFizz'),
    ("1\n5", '1\n2\nFizz\n4\nBuzz'),
    ("12\n15", 'Fizz\n13\n14\nFizzBuzz'),
    ("9999\n10000", 'Fizz\nBuzz'),
])
def test_fizzbuzz_positive(corrrect_input, expected_output):
    assert fizzbuzz(corrrect_input) == expected_output


@pytest.mark.parametrize("wrong_input_format, exception_type", [
    ("1", ValueError),
    ("1\n3\n5", ValueError),
    ("1\na", ValueError),
])
def test_fizzbuzz_wrong_input_format(wrong_input_format, exception_type):
    with pytest.raises(exception_type) as e:
        fizzbuzz(wrong_input_format)
    assert e is not None

@pytest.mark.parametrize("wrong_input_values, exception_type", [
    ("-1\n0", ValueError),
    ("0\n1", ValueError),
    ("10000\n10001", ValueError),
    ("10001\n10002", ValueError),
    ("3\n3", ValueError),
    ("5\n3", ValueError),
])
def test_fizzbuzz_values_out_of_range(wrong_input_values, exception_type):
    with pytest.raises(exception_type) as e:
        fizzbuzz(wrong_input_values)
    assert e is not None
