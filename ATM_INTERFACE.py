class GeneralBankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            return True
        else:
            print("Fund is not sufficient!")
            return False


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def display_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

    def handle_option(self, option):
        if option == 1:
            withdraw_amount = float(input("Enter withdrawal amount: "))
            if withdraw_amount > 0:
                self.bank_account.withdraw(withdraw_amount)
            else:
                print("Amount entered is not valid!")

        elif option == 2:
            deposit_amount = float(input("Enter deposit amount: "))
            if deposit_amount > 0:
                self.bank_account.deposit(deposit_amount)
            else:
                print("Amount entered is not valid!")

        elif option == 3:
            print(f"Current Balance: ${self.bank_account.get_balance()}")

        elif option == 4:
            print("Exiting ATM. Thank you!")
            exit()

        else:
            print("Option is not valid!")


# Main Program
if __name__ == "__main__":
    user_account = GeneralBankAccount(1000.0)  # Initial balance
    atm = ATM(user_account)

    while True:
        atm.display_menu()
        try:
            choice = int(input("Enter your choice: "))
            atm.handle_option(choice)
        except ValueError:
            print("Please enter a valid number!")
