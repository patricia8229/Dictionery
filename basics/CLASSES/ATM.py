#creating a new class
#read on principals of OOP

class Bank:
    name ="Equity"

class ATMCard(Bank):
    #Bank.name =
    #this is a property
    #a class variable/data member
    #a class variable is shared among all instances of class
    colour = "Brown"
    balance = 0

    #actions are called methods in python
    #methods are just functions, only that they are inside a class
    #a constractor is a special method that runs every time you inatantiate
    #in python
    def __init__(self,op__balance):
        self
    def deposit(self,amount):


        self.balance += amount
        print("Deposited ",amount)
    def withdraw(self,amount):
        if self.balance < amount:
            print("Sorry Insufficient")
        else:
            self.balance -= amount
            print("Success:{}",format(amount))



