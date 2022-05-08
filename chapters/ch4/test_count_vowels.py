from chapters.ch4.count_vowels import count_vowels


def test_count_vowels():
    word = 'blughesArthioasutuys'
    output = count_vowels(word)
    assert output == 9

def test_count_zero_vowels():
    word = 't'
    output = count_vowels(word)
    assert output == 0