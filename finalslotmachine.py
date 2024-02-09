import ntpath
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
winnings = 0


def check_winnings(columns, lines, bet, values):
    
    global winnings
    winnings=0
    print("wiinings= ", winnings)
    winning_lines = []

    for i in range(lines):

        if columns[0][i] == columns[1][i] == columns[2][i]:
            print("Yay, you won on lines", i+1)
            winnings += values[columns[0][i]] * bet

        else:
            print("Sorry, you did not win on lines", i+1)
    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= MAX_BET:
                break
            else:
                print("Amount must be greater between 0 and 100!")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:

                break

            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}!")
        else:
            print("Please enter a number")

    return amount


def main(n):
    balance = deposit()

    while True:

        lines = get_number_of_lines()
        while True:
            bet = (get_bet())
            total_bet = bet * lines

            if total_bet > balance:
                n = 0
                print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
                break
            else:
                n = 2
                break
        if n == 0:
            main(n)
            break

        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings=0
        winnings = check_winnings(slots, lines, bet, symbol_value)
        print("winnings is: ", winnings)
        if winnings != 0:

            balance -= total_bet
            balance += winnings
        else:
            balance -= total_bet

        print("Total balance is: ", balance)

        if balance >= 1:
            ans = input("Do u want to continue playing? (y/n):")
            if ans in ['y', 'Y']:
                continue
            else:
                break
        else:
            break


main(1)