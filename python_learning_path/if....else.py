""" If...else Statements in Python are used for conditional execution of code blocks based on whether a condition is True or False. 
They allow you to control the flow of your program by executing different code paths depending on certain conditions.

The basic syntax of an if...else statement is as follows:

if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if condition is False

Identation is crucial in Python, as it defines the scope of the code blocks associated with the if and else statements.
"""
print(__doc__, "\n")

a = 10
b = 20
print("The value of a is ", a, "\n and the value of b is ", b, "\n")

if a < b:
    print("a is less than b")


putItin = input("\nWould you like to compare two numbers? (yes/no): ").strip().lower()
if putItin == "yes":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")
else:
    print("okay, maybe next time!")

print("\nThank you for using the comparison tool!")

""" short-hand if...else statement, also known as the ternary operator, allows you to write an if...else statement in a single line.
The syntax for the short-hand if...else statement is as follows:
"""
print(__doc__, "\n")

numb = int(input("Enter a number to check if it's even or odd: "))
result = "Even" if numb % 2 == 0 else "Odd"
print(f"The number {numb} is {result}.")

