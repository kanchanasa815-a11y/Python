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
 
