def sum_pennies(user_input):
    return int(user_input)


def sum_nickels(user_input):
    return 5 * int(user_input)


def sum_dimes(user_input):
    return 10 * int(user_input)


def sum_quarters(user_input):
    return 25 * int(user_input)


def sum_all_coins(pennies, nickels, dimes, quarters):
    for i in (pennies, nickels, dimes, quarters):
        if not str.isnumeric(i):
            return None

    return sum([sum_pennies(pennies),
                sum_nickels(nickels),
                sum_dimes(dimes),
                sum_quarters(quarters)
                ])


def generate_result(total):
    if total == 100:
        return 'You win.'

    if total < 100:
        under = 100 - total
        return f'You lose... you were under by {under} cents.'

    if total > 100:
        over = total - 100
        return f'You lose... you were over by {over} cents.'
