class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(self.name,int_rate=.02,account_balence=200)
    def make_deposit(self, amount):
        self.account.make_deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.make_withdrawl(amount)
        return self
    def display_user_balance(self):
        print('Account name:',self.name,'- Your balance is: $'+str(self.account.display_account_info()))

class BankAccount:

    def __init__(self,name,int_rate,account_balence=0):
        self.name=name
        self.account_balance=account_balence
        self.int_rate=int_rate

    def make_deposit(self, amount):
        self.account_balance +=amount 

    def make_withdrawl(self, amount):
        if (self.account_balance - amount)<0:
            print('Account name:',self.name,'- Not enough money in account for request of $'+str(amount))
        self.account_balance -= amount

    def display_account_info(self):
        print('Account name:',self.name,'- Your balance is: $'+str(self.account_balance))

    def yield_interest(self):
        self.account_balance += (self.account_balance * self.int_rate)