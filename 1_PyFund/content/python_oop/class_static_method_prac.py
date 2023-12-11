class BankAccount:
    # ! delcare class attributes here
    # shared among all bank accounts
    bank_name = "Lucido Bank & Trust"
    all_accounts = []

    # ! constructor function here
    # create the instance of an object
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    # ! class attributes are more flexible because we can change them on the entire class or its instance

    @classmethod
    # clas method to change bank name
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    # class method to get all balances of all accounts
    def get_all_balances(cls):
        total_sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            total_sum += account.balance
        return sum  

    # ! class methods have no access to the instance attribute or any attribute that starts with 'self'
    # ! static methods have no access to neither class nor instance attributes, so they would need to pass through arguments only

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True