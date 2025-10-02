class BankAccount:
    def __init__(self, initial_balance=0):
        # "Private" attribute (by convention, underscore means internal use)
        self._account_balance = initial_balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount

    # Withdraw money if sufficient funds exist
    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount <= self._account_balance:
            self._account_balance -= float(amount)
            return True
        else:
            return False

    # Display current balance
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")
