rint("Simple Caluclator")
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
while(True):
    choice=int(input("Enter the choice(1-5):"))
    if choice==1:
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print(num1+num2)
    elif choice==2:
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print(num1-num2)
    elif choice==3:
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print(num1*num2)
    elif choice==4:
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print(num1/num2)
        break
    else:
        print("Exiting the calculatoor.GoodBye!")
 Output:
Simple Caluclator
1.Addition
2.substraction
3.Multiplication
4.Division
5.Exit
Enter the choice(1-5):5
Exiting the calculatoor.GoodBye!

def menu():
    print("Welcome to the Menu-Driven Program!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        print("You selected Option 3.")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
Output:
Welcome to the Menu-Driven Program!
1. Option 1
2. Option 2
3. Option 3
4. Exit
Enter your choice (1-4): 4
Exiting the program. Goodbye!

print("Simple Caluclator")
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
while(True):
    
        choice=int(input("Enter the choice(1-5):"))
        if choice in {1,2,3,4}:
               num1=int(input("Enter the number1: "))
               num2=int(input("Enter the number2: "))
               if choice==1:
                     print(num1+num2)
               elif choice==2:
                     print(num1-num2)
               elif choice==3:
                     print(num1*num2)
               elif choice==4:
                      print(num1/num2)
               break

        else:
              print("Exiting the calculatoor.GoodBye!")
QUESTION:
Banking System: Write a menu-driven program to simulate a basic banking system with options like:

Check Balance
Deposit Money
Withdraw Money
Exit

print("Banking system")
print("1.Check Balance")    
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")
balance=0
while True:
    choice=int(input("Enter the choice:  "))
    if choice in {1,2,3,4}:
        if choice ==1:
            print("Balance is checking",balance)
        elif choice==2:
            amount=int(input("Enter the amount to deposit: "))
            balance+=amount
            print("Deposit Money")
        elif choice==3:
            amount=int(input("Enter the amount to Withdraw: "))
            if balance>amount:
                balance-=amount
            else:
                print('Insufficient amount')
            
        elif choice==4:
             print("Exit form the Banking system")
             break
        else:
            print("There is no any Update.......")
OUTPUT:
Banking system
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit
Enter the choice:  1
Balance is checking 0
Enter the choice:  2
Enter the amount to deposit: 800
Deposit Money
Enter the choice:  3
Enter the amount to Withdraw: 90
Enter the choice:  4
Exit form the Banking system

QUESTION:
Grocery Store Menu:

Create a program where users can:
Add items to their cart.
Remove items.
View the total price.
Exit.

    def menu():
    print("------Grocery Store-------")
    print("1.Add the items to their cart")
    print("2.Remove items")
    print("3.View the total Price")
    print("4.Exit")

cart=0
total_price=0
while(True):
    menu()
    choice=int(input("Enter the Choice:  "))
    if choice==1:
        add=int(input("Enter the number of item: "))
        price=int(input("Enter item price:"))
        cart+=add
        total_price+=add*price
        print("cart= ",cart)
        print("total price",total_price)
    elif choice==2:
        cancle_item=int(input("Enter the number to remove the item: "))
        if cart>=cancle_item:
            price = int(input("Enter the price of one item to remove: "))
            cart-=cancle_item
            total_price-=cancle_item*price
            print("Removed the item",cart)
        else:
            print("Insufficent cart")
    elif choice==3:

        print("View the total price",total_price)
    elif choice==4:
        print("Exit for there.....")
        break
    else:
        print("There is no other choice you can exit form here")
    
OUTPUT:
------Grocery Store-------
1.Add the items to their cart
2.Remove items
3.View the total Price
4.Exit
Enter the Choice:  1
Enter the number of item: 8
Enter item price:50
cart=  8
total price 400
------Grocery Store-------
1.Add the items to their cart
2.Remove items
3.View the total Price
4.Exit
Enter the Choice:  2
Enter the number to remove the item: 3
Enter the price of one item to remove: 50
Removed the item 5
------Grocery Store-------
1.Add the items to their cart
2.Remove items
3.View the total Price
4.Exit
Enter the Choice:  3
View the total price 250
------Grocery Store-------
1.Add the items to their cart
2.Remove items
3.View the total Price
4.Exit
Enter the Choice:  4
Exit for there.....

QUESTION:
Educational System:

Write a program with options to:
Add student details.
Display student details.
Exit.


class Student:
            def __init__(self,usn,name,sem):
                self.usn=usn
                self.name=name
                self.sem=sem
            def display_info(self):
                print("USN:" ,self.usn)
                print("Name:" ,self.name)
                print("sem:", self.sem)
print("<<<<<<<<<Eduction System>>>>>>>>>>>")
student=None
while True:
    print("\n1.Add STudent Details")
    print("2.Display Student Details")
    print("3.Exit")


    choice=int(input("Enter the choice: "))
    if choice==1:
        usn=int(input("ENter the student usn: "))
        name=input("ENter the name: ")
        sem=int(input("Enter the sem: "))
        student=Student(usn,name,sem)
        print("Student details added successfully!")
    elif choice==2:
         if student:
            student.display_info()
         else:
              print("No student details available.")
         
             
    elif choice==3:
        print("Exit")
        break
    else:
        print("No more choice.....")

OUTPUT:
<<<<<<<<<Eduction System>>>>>>>>>>>

1.Add STudent Details
2.Display Student Details
3.Exit
Enter the choice: 1
ENter the student usn: 043
ENter the name: kanchana
Enter the sem: 7
Student details added successfully!

1.Add STudent Details
2.Display Student Details
3.Exit
Enter the choice: 2
USN: 43
Name: kanchana
sem: 7

1.Add STudent Details
2.Display Student Details
3.Exit
Enter the choice: 3
Exit




 
