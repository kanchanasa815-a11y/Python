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



 
