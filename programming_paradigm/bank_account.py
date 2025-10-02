class BankAccount:
    def __init__(self, initial_balance=0):
        # "Private" attribute (by convention, underscore means internal use)
        self._account_balance = initial_balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money if sufficient funds exist
    def withdraw(self, amount):
        if amount <= 0:
            print("You have insufficient balance.")
            return False
        if amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds. Withdrawal denied.")
            return False

    # Display current balance
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")
