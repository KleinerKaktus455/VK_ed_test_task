import pytest


def float_addition(float1, float2):
    sum_result = float1 + float2
    return sum_result


@pytest.mark.parametrize('float1,float2',
                         [
                             (1, 2),
                             (1.1, -4.5),
                             (-4.5, 17),
                             (-1.1, -2.3),
                             (0, 1.1),
                             (-1.1, 0)
                         ])
def test_float_addition(float1, float2):
    sum_function_result = float_addition(float1, float2)
    sum_result = float1 + float2
    assert sum_result == sum_function_result, "Unexpected function value"


@pytest.mark.xfail(reason="Negative test")  # Condition 3: "Все тесты должны проходить"
def test_float_addition_with_incorrect_arguments():
    argument1_incorrect = 'ъ'
    argument2 = 1.31
    assert float_addition(argument1_incorrect, argument2)


def len_str(string):
    len_string = 0
    for letter in string:
        len_string += 1
    return len_string


def test_len_string_function():
    test_string = 'some_string'
    len_string = len_str(test_string)
    assert len(test_string) == len_string, "String length calculated incorrectly!"


def test_lower_string_method():
    test_string = 'SOMESTRING'
    test_string = test_string.lower()
    assert test_string.islower(), "String contains capital letters!"


def test_clear_dict_method():
    test_dict = {'some_key': 'some_value'}
    test_dict.clear()
    assert test_dict == {}, "Data from dictionary is not deleted!"


def test_get_value_from_dict_by_key():
    test_value = 'some_data'
    test_key = 'some_key'
    test_dict = {test_key: test_value}
    assert test_dict[test_key] == test_value, "Received data from dictionary is not correct!"
