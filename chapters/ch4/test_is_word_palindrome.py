import pytest

from chapters.ch4.is_word_palindrome import is_word_palindrome

examples = [(False, 'LAGLglskjgls'),
            (True, 'gaG'),
            (True, 'Madam'),
            (True, ''),
            (True, '65656')]

@pytest.mark.parametrize('is_palindrome, word', examples)
def test_is_palindrome(is_palindrome, word):
    output = is_word_palindrome(word)
    assert is_palindrome == output
