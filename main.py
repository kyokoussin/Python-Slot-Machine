import random
import time

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    weights = [ 15,  10,   5,   4,    3]

    return [random.choices(symbols, weights= weights)[0] for symbol in range(3)]

def print_row(row):
    print("Spinning...\n")
    print("*************************")
    print("| ", end="")

    for x in range(3):
        time.sleep(1 + x/5)
        print(row[x], end= " | ")
    print("\n*************************")
    time.sleep(0.3)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍒':
                return bet * 3
            case '🍉':
                return bet * 4
            case '🍋':
                return bet * 5
            case '🔔':
                return bet * 10
            case '⭐':
                return bet * 25

    return 0

def main():
    balance = 1000

    print("*************************")
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: CHF {balance:,}".replace(",", "'"))

        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number: ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won CHF {payout} !!!")
        else:
            print("Sorry you lost this round...")

        balance += payout

        play_again = input("Do you want to spin again? ")
        if play_again not in ['Y', 'y', 'Yes', 'yes', 'YES']:
            break

    print("\nThank you for playing my game!")
    print(f"Your final balance is CHF {balance}!")

if __name__ == '__main__':
    main()