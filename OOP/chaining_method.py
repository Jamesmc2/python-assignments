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
James=User('James','James@gmail.com')
Michael=User('Michael','M@gmail.com')
Anna=User('Anna','Anna@gmail.com')
James.make_deposit(100).make_deposit(200).make_deposit(150).make_withdrawl(50).display_user_balance()

Michael.make_deposit(500).make_deposit(300).make_withdrawl(200).make_withdrawl(400).display_user_balance()

Anna.make_deposit(150).make_withdrawl(100).make_withdrawl(25).make_withdrawl(30).display_user_balance()
