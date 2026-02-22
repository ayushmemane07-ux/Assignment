#info of bankaccount
class bankaccount:
    def __init__(self, account_number,balance=0.0):
        self.account_number=account_number
        self.balance=balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited:{amount}.new balance{self.balance}")
        else:
            print(f"deposited amount must be positive")

    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"withdraw:{amount}.******new balance{self.balance}")
            else:
                print(f"insufficient balance")
        else:
            print(f"withdraw amount must be positive")

    def check_balance(self):
        print(f"Account:{self.account_number} ******balance:{self.balance}")

#Example usage 
if __name__ == "__main__":
    account = bankaccount("123456789123",54000)
    account.check_balance
    account.deposite(6000)
    account.withdraw(4000)

    account.check_balance()
