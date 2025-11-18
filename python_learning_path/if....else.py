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

""" We also have the  logical operators 'and', 'or', and 'not' that can be used to combine multiple conditions in if...else statements.
- 'and' operator returns True if both conditions are True.
- 'or' operator returns True if at least one condition is True.
- 'not' operator negates the condition, returning True if the condition is False.
"""
print(__doc__, "\n")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship (yes/no): ").strip().lower()

if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
elif age < 18 or citizenship == "no":
    print("You are not eligible to vote yet, you must be at least 18 years old.")
elif age >= 18 and citizenship == "no":
    print("You are not eligible to vote, you must be a citizen.")
elif citizenship == "no":
    print("You must be a citizen to vote.")
else:
    print("Invalid input.")

print("\nThank you for using the voting eligibility checker!")


""" Nested if...else statements are if...else statements that are contained within another if or else block."""

print(__doc__, "\n")
num = int(input("Enter a number to check if it's positive, negative, or zero: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    elif num > 0:
        print("The number is positive.")
else:
    print("The number is negative.")

""" You can also use logical operators with nested if...else statements to create more complex conditions."""
print(__doc__, "\n")
score = int(input("Enter your score (0-100): "))
if score >= 0 and score <= 100:
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")


""" In python we also have the pass statement that can be used as a placeholder in if...else statements when no action is required."""
print(__doc__, "\n")

number = int(input("Enter a number: "))
if number > 0:
    pass  # Placeholder for future code
else:
    print("The number is not positive.")

print("\nThank you for using the number checker!")