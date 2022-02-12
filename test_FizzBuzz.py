import pytest
from FizzBuzz import fizzbuzz


def test_fizzbuzz_has_input_argument():
    assert 'input' in fizzbuzz.__annotations__.keys()


def test_fizzbuzz_has_return_statement():
    assert 'return' in fizzbuzz.__annotations__.keys()
    assert str(fizzbuzz.__annotations__['return']) == "<class 'str'>"


@pytest.mark.parametrize("corrrect_input, expected_output", [
    ("1\n2", '1\n2'),
    ("1\n3", '1\n2\nFizz'),
    ("1\n5", '1\n2\nFizz\n4\nBuzz'),
    ("12\n15", 'Fizz\n13\n14\nFizzBuzz'),
    ("9999\n10000", 'Fizz\nBuzz'),
])
def test_fizzbuzz_positive(corrrect_input, expected_output):
    assert fizzbuzz(corrrect_input) == expected_output


@pytest.mark.parametrize("wrong_input_format, exception_statement", [
    ("1", "not enough values to unpack (expected 2, got 1)"),
    ("1\n3\n5", 'too many values to unpack (expected 2)'),
    ("1\na", "invalid literal for int() with base 10: 'a'"),
])
def test_fizzbuzz_wrong_input_format(wrong_input_format, exception_statement):
    with pytest.raises(ValueError) as e:
        fizzbuzz(wrong_input_format)
    assert e.value.args[0] == exception_statement


@pytest.mark.parametrize("wrong_input_values, expected_output", [
    ("-1\n0", "values don't satisfy condition 1 <= n < m <= 10000"),
    ("0\n1", "values don't satisfy condition 1 <= n < m <= 10000"),
    ("10000\n10001", "values don't satisfy condition 1 <= n < m <= 10000"),
    ("10001\n10002", "values don't satisfy condition 1 <= n < m <= 10000"),
    ("3\n3", "values don't satisfy condition 1 <= n < m <= 10000"),
    ("5\n3", "values don't satisfy condition 1 <= n < m <= 10000"),
])
def test_fizzbuzz_values_out_of_range(wrong_input_values, expected_output):
    with pytest.raises(ValueError) as e:
        fizzbuzz(wrong_input_values)
    assert e.value.args[0] == expected_output
