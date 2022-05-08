from chapters.ch3 import coins


def change_for_dollar():
    print("GAME: Change for Dollar")
    print("If the change sums up to exactly 1 dollar, you win.")

    pennies = input("Enter number of pennies: ")
    nickels = input("Enter number of nickels: ")
    dimes = input("Enter number of dimes: ")
    quarters = input("Enter number of quarters: ")

    total = coins.sum_all_coins(pennies, nickels, dimes, quarters)

    if total:
        print(coins.generate_result(total))
    else:
        print('Invalid input. You should enter numbers')
        quit(1)


if __name__ == '__main__':
    change_for_dollar()