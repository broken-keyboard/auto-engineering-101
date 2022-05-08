from chapters.ch2.add_number import add, is_even, is_positive, convert_to_number


def test_convert_str_to_int():
    number = convert_to_number('5')
    assert number == 5

def test_convert_nonnumeric_str_to_int_fails():
    assert convert_to_number('a') is None

def test_is_even():
    assert is_even(5) is False
    assert is_even(4)

def test_is_positive():
    assert is_positive(1)
    assert is_positive(-1) is False

def test_adding_even_nums_returns_even():
    number = add(2, 2)
    assert is_even(number)

def test_adding_two_uneven_nums_returns_even():
    number = add(3, 3)
    assert is_even(number)

def test_adding_even_and_uneven_returns_uneven():
    number = add(5, 4)
    assert is_even(number) is False

def test_adding_two_negative_nums_returns_negative():
    number = add(-1, -1)
    assert is_positive(number) is False
"""
def test_adding_str_and_int_fails():
    fail = add('carlos', 2)
    assert fail == 'Cannot add string and integer'
"""