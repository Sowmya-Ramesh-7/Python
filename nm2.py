import random
import sys
def otp():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    print("your otp is ",otp)
    print("Enter your otp to continue the transaction :")
    x=input()
    if otp==x:
        print("Proceed with the transaction");
        return;
    else:
        print("Invalid otp")
        sys.exit()
        

class ATM():
    def __init__(self,balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: ", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} withdrawal successful!")
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        print("Available balance: ", self.balance)
        print()

    def transaction(self):
        print( "Enter the choice :\n1. Balance enquiry \n2. Withdrawal\n3. Cash deposit\n4. Exit\n")
        while True:
            opt = int(input("Enter 1, 2, 3, or 4:"))
            otp()
            if opt == 1:
                atm.check_balance()
            elif opt == 2:
                amount = int(input("How much you want to deposit:"))
                atm.deposit(amount)
            elif opt == 3:
                amount = int(input("How much you want to withdraw:"))
                atm.withdraw(amount)
            elif opt == 4:
                print(" Thanks for choosing us as your bank")
                sys.exit()
            else:
                print("Error: Enter 1, 2, 3, or 4 only!\n")
                continue
                
username="XYZ"
password =123
balance=1000
print("WELCOME")
name = input("Enter your name: ")
atmpin = int(input("Enter your ATM pin: "))
if username==name and password== atmpin:
    atm = ATM(balance)
    atm.transaction()
else:
    print("Invalid username or password")
