print("Simple Caluclator")
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
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
