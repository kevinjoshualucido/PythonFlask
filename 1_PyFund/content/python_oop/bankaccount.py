class BankAccount:
    # ! delcare class attributes here
    # shared among all bank accounts
    all_accounts = []

    # ! constructor function here
    # create the instance of an object
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Deposit amount:", amount)
        self.balance += amount
        return self

    def withdraw(self, amount):
        if not amount > self.balance:
            print("Withdrawal amount:", amount)
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Total account balance:", self.balance)
        return self

    def yield_interest(self):
        interest_earned = self.balance * self.interest_rate
        print("Interest earned:", interest_earned)
        self.balance += interest_earned
        return self
    
    @classmethod
    # display all instances of bank account's info
    def display_all_accounts(cls):
        print("--Display all account balances:--")
        for account in cls.all_accounts:
            account.display_account_info()


# # ! instantiate objects here
# # create two bank accounts
# account1 = BankAccount(0.05, 1_000)
# account2 = BankAccount(0.0125, 500)

# # ! chaining method
# # account1 makes 3 deposits and 1 withdrawal, yield interest, and then display account info
# print("--Account 1--")
# account1.deposit(250).deposit(1_000).deposit(895).withdraw(620).yield_interest().display_account_info()
# # account2 makes 2 deposits and 4 withdrawals, yield interest, and then display account info
# print("--Account 2--")
# account2.deposit(1_150).deposit(950).withdraw(550).withdraw(250).withdraw(85).withdraw(15).yield_interest().display_account_info()

# # display all instances of bank account's info
# BankAccount.display_all_accounts()