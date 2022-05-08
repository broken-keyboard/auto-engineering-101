import pytest
from chapters.ch3 import coins


def test_sum_pennies():
    total = coins.sum_pennies(user_input='50')
    assert total == 50

def test_sum_nickels():
    total = coins.sum_nickels(user_input='5')
    assert total == 25

def test_sum_dimes():
    total = coins.sum_dimes(user_input='2')
    assert total == 20

def test_sum_quarters():
    total = coins.sum_quarters(user_input='3')
    assert total == 75

def test_sum_all_coins():
    total = coins.sum_all_coins(pennies='1', nickels='1', dimes='1', quarters='1')
    assert total == 41

def test_sum_all_coins_not_numeric():
    total = coins.sum_all_coins(pennies='a', nickels='b', dimes='c', quarters='1')
    assert total is None

def test_win_exact_dollar():
    total = 100
    message = coins.generate_result(total)
    assert message == 'You win.'


def test_lose_under_dollar():
    total = 70
    message = coins.generate_result(total)
    assert message == f'You lose... you were under by 30 cents.'


def test_lose_over_dollar():
    total = 140
    message = coins.generate_result(total)
    assert message == f'You lose... you were over by 40 cents.'
