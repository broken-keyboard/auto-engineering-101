def convert_to_number(s):
    if str.isnumeric(s):
        return int(s)
    print('Invalid input: not numeric')

def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return 'Cannot add string and integer'
    return x + y


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def is_positive(num):
    if num >= 0:
        return True
    return False


def challenge_1():
    input_1 = input('Enter a number: ')
    num_1 = convert_to_number(input_1)
    if not num_1:
        quit(1)
    input_2 = input('Enter another number: ')
    num_2 = convert_to_number(input_2)
    if not num_2:
        quit(1)
    total = add(num_1, num_2)
    print(total)


if __name__ == '__main__':
    challenge_1()