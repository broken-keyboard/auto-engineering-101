'''
Travel the entire game board of 20 spaces within 5 die rolls.
WIN: Roll a total of 20 or more within 5 rolls
LOSE: Roll a total of less than 20 within 5 rolls
'''

import random


def roll_the_die_game(max_rolls):
    rolls_remaining = max_rolls
    board_size = 20
    space_num = 0
    while 0 < rolls_remaining <= max_rolls:
        die_num = roll_die()
        space_num += die_num

        msg = evaluate_result(rolls_remaining, space_num, board_size)
        print(f"You rolled a {die_num}. {msg}")

        rolls_remaining -= 1


def evaluate_result(rolls_remaining, space_num, board_size):
    #print(rolls_remaining, die_num, space_num, board_size)
    space_remaining = board_size - space_num
    if space_num >= board_size:
        return f"Congratulations, you reached the end."
    if rolls_remaining == 0:
        return 'You did not reach the end ...'
    return f"You are now on space {space_num} and have {space_remaining} spaces to go."


def roll_die():
    return random.randrange(1, 7, 1)


if __name__ == '__main__':
    print('Roll the die to reach the end of the board!')
    roll_the_die_game(max_rolls = 5)