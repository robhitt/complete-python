class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {str(self.balance)}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Funds Unavailable")
            return

        self.balance -= withdrawal_amount
        print("Withdrawal Accepted")


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdrawal(75)
acct1.withdrawal(500)

