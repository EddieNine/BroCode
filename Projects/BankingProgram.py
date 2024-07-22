

def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        print(f'You deposited: ${amount:.2f}')
        return amount
def withdraw(balance):
    amount = float(input("Enter your amount to be withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print(f'You withdrew: ${amount:.2f}')
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("-="*20)
        print('''           BANKING PROGRAM''')
        print("-="*20)
        print('''1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit''')

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("That is not a valid choice")
    print("Thank you! have a nice day!")

if __name__ == '__main__':
    main()