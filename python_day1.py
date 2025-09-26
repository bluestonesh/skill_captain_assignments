class BankAccount:
    def __init__(self, account_number, account_holder, account_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount>0:
            self.account_balance += amount
            print(f"{amount} has been added to your account.")
        else:
            print("Amount must be greater than 0")
    def withdraw(self, amount):
        if amount and self.account_balance >0:
            self.account_balance -= amount
            print(f"{amount} has been withdrawn from your account.")
        else:
            print("Amount must be greater than 0")
    def display_info(self):
        print(f"Account holder {self.account_holder}")
        print(f"Account number {self.account_number}")
        print(f"Account balance {self.account_balance}")
