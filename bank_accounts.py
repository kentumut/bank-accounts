class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created. \nBalance = {self.balance:.2f}")