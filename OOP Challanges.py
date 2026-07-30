1.Banking System Simulation
Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.

Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
Emphasize encapsulation, inheritance and polymorphism.

class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0    #Encapsulation
    def check_balance(self):
        print(f"balance: {self._balance}")
    def deposit(self,amount):
        self._balance+=amount
        print(f"Amount: {amount} new_Balance: {self._balance}")
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print("Withdraw Sussesfully")
        else:
            print("Insufficent balance")

class saving_account(Account):
    def calucalate_interest(self):
        INTERESTRATE=0.04
        interest=self._balance * INTERESTRATE
        print(f"Interest: {interest}")
class Current_account(Account):
    def withdraw(self,amount):   #Ploymorphesim
            OVERDRAFT_LIMIT=1000
            if self._balance+OVERDRAFT_LIMIT>=amount:
                self._balance-=amount
                print("Withdraw Sussesfully")
            else:
                print("Insufficent balance")
    
class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}
    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_account=saving_account(id,holder_name)
        elif type=="current":
             new_account=Current_account(id,holder_name)
        self.__account[id]=new_account
        print('Account creation succesfully')
        return new_account
    def get_account(self,id):
        if id not in self.__account:
            print("Account not found")
        else:
            account=self.__account[id]
            print(f"\nID: {account.id}\n Holder Name : {account.holder_name}")
            return account
kbk=Bank("Kanchana bank of Karnataka","Hospet")
s1=kbk.create_account("1","Tharun","savings")
c1=kbk.create_account("2","Virate","current")
s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.calucalate_interest()

OUTPUT:
Account creation succesfully
Account creation succesfully
Amount: 1000 new_Balance: 1000
Amount: 10 new_Balance: 10
Insufficent balance
Withdraw Sussesfully
Interest: 40.0
