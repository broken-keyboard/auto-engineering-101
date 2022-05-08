from chapters.ch4.roll_the_die_game import roll_the_die_game, evaluate_result


def test_roll_the_die_game_exact_20():
    msg = evaluate_result(rolls_remaining=0, space_num=20, board_size=20)
    assert 'Congratulations' in msg


def test_roll_the_die_game_finish_under_20():
    msg = evaluate_result(rolls_remaining=0, space_num=19, board_size=20)
    assert 'did not reach' in msg


def test_roll_the_die_game_over_20():
    msg = evaluate_result(rolls_remaining=0, space_num=21, board_size=20)
    assert 'Congratulations' in msg


def test_roll_the_die_game_continue_loop():
    rolls_remaining = [1,2,3,4,5]
    for i in rolls_remaining:
        msg = evaluate_result(rolls_remaining=i, space_num=19, board_size=20)
        assert 'now on space' in msg
