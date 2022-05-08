from chapters.ch2.seasons import get_season


def test_input_winter_return_snow():
    answer = get_season('winter')
    assert answer == 'snow'


def test_input_spring_return_flowers():
    assert get_season('spring') == 'flowers'


def test_input_summer_return_beach():
    assert get_season('summer') == 'beach'


def test_input_autumn_return_leaves():
    assert get_season('autumn') == 'leaves'


def test_input_unknown_season_return_unknown():
    assert get_season('blah') == "I don't know that season"