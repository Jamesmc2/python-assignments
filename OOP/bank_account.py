class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance +=amount
        return self
    def make_withdrawl(self, amount):
        if (self.account_balance - amount)<0:
            print('Account name:',self.name,'- Not enough money in account for request of $'+str(amount))
            return self
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('Account name:',self.name,'- Your balance is: $'+str(self.account_balance))

class BankAccount:

    def __init__(self,name,int_rate,account_balence=0):
        self.name = name
        self.account_balance=account_balence
        self.int_rate=int_rate

    def make_deposit(self, amount):
        self.account_balance +=amount
        return self

    def make_withdrawl(self, amount):
        if (self.account_balance - amount)<0:
            print('Account name:',self.name,'- Not enough money in account for request of $'+str(amount))
            return self
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print('Account name:',self.name,'- Your balance is: $'+str(self.account_balance))
        return self

    def yield_interest(self):
        self.account_balance += (self.account_balance * self.int_rate)
        return self



James=BankAccount('James',.04,account_balence=200)
Anna=BankAccount('Anna',.02,account_balence=400)

James.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawl(200).yield_interest().display_account_info()

Anna.make_deposit(200).make_deposit(100).make_withdrawl(50).make_withdrawl(80).make_withdrawl(30).make_withdrawl(200).yield_interest().display_account_info()
