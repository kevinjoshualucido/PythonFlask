from bankaccount import BankAccount


# User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def display_user_info(self):
        print(self.name, self.email, self.accounts)
        return self

    def open_checking_account(self):
        new_account = BankAccount(interest_rate=0.02, balance=0)
        self.accounts["Checking"] = new_account
        return self

    def open_savings_account(self):
        new_account = BankAccount(interest_rate=0.05, balance=0)
        self.accounts["Savings"] = new_account
        return self

    def make_deposit(self, account, amount):
        print(self.name)
        self.accounts[account].deposit(amount)
        return self

    def make_withdrawal(self, amount):
        print(self.name)
        self.account.withdraw(amount)
        return self


user1 = User("Kevin Lucido", "kevinlucido@gmail.com")

user1.open_checking_account()
user1.make_deposit("Checking", 100)

user1.display_user_info()