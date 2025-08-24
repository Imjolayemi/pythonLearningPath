""" This  modulle is all about operators in python
operators are divided into the below groups
    1. Arithmetic operators
    2. Assignment operators
    3. Comparison operators
    4. Logical operators
    5. Identity operators
    6. Membership operators
    7. Bitwise operators
    8. Operator precedence
"""
"""
1. Arithmetic operators
below are the types of arithmetic operators
    1. Addition
    2. subtraction
    3. multiplication
    4. Division
    5. modulus
    6. Exponential
    7. Floor Division
"""

a = 15
b = 10

# Addition
print("\n The Addition of", a, "and", b, "is",a+b, "\n") # this prints the addition of the variables

# Subtraction
print("The Subtraction of", a, "and", b, "is",a-b, "\n") # this print the subtraction of the variables

# multiplication
print("The Multiplication of", a, "and", b, "is",a*b, "\n") # this print the Multiplication of the variables

# Division
print("The Division of", a, "and", b, "is",a/b, "\n") # this print the Division of the variables

# Modulus
print("The Modulus of", a, "and", b, "is",a%b, "\n") # this print the Modulus of the variables

# Floor Division
print("The Floor Division of", a, "and", b, "is",a//b, "\n") # this print the Floor Division of the variables

# Exponential
print(a, "Exponential", b, "is",a**b, "\n") # this print the Exponential of the variables

"""
2. Assignment Operators
    Below are the Assignmentg Operators in python
    =
    +=
    -=
    *=
    /=
    %=
    **=
    //=
    &=
    |=
    ^=
    <<=
    >>=
    :=
"""
Assignment_Operators = """
The below operations are types/Groups of Assignment Operators in Python.
And how they works"""

print(Assignment_Operators, "\n") # prints the variable

print(a, "+=", b,)
a+=b # The value of a changes by adding b to it
print("a is now ", a, "\n")

print(a, "-=", b,)
a-=b # The value of a changes by subtracting b from it
print("a is now ", a, "\n")

print(a, "*=", b,)
a*=b # The value of a changes by multiplying b to it
print("a is now ", a, "\n")

print(a, "/=", b,)
a/=b # The value of a changes by dividing b to it
print("a is now ", a, "\n")

print(a, "%=", b,)
a%=b # The value of a changes by getting the modulus of b to it
print("a is now ", a, "\n")

print(a, "**=", b,)
a**=b # The value of a changes by getting the Exponential of b to it
print("a is now ", a, "\n")

print(a, "//=", b,)
a//=b # The value of a changes by getting the Floor Division of b to it
print("a is now ", a, "\n")

#a&=b # The value of a changes by getting the Bitwise AND of b to it
print(a, "&=", b, "=", a, "\n", "a is now ", a, "\n")

# a|=b # The value of a changes by getting the Bitwise OR of b to it
# print(a, "|=", b, "=", a, "\n", "a is now ", a, "\n")

# a^=b # The value of a changes by getting the Bitwise XOR of b to it
# print(a, "^=", b, "=", a, "\n", "a is now ", a, "\n")

# a<<=b # The value of a changes by getting the Bitwise Left Shift of b to it
# print(a, "<<=", b, "=", a, "\n", "a is now ", a, "\n")

# a>>=b # The value of a changes by getting the Bitwise Right Shift of b to it
# print(a, ">>=", b, "=", a, "\n", "a is now ", a, "\n")

print(a, ":=", b,)
(a := b) # The value of a changes by getting the Assignment Expression of b to it
print("a is now ", a, "\n")



"""
3. Comparison Operators
    Below are the Comparison Operators in python
    ==
    !=
    >
    <
    >=
    <=
"""
Comparison_Operators = """ 
Comparison Operators are used to compare two values and they return a boolean value.
The below operations are types/Groups of Comparison Operators in Python."""
print(Comparison_Operators, "\n") # prints the variable
a = 15
b = 10
if a == b:
    print(a, "==", b, "is False" "\n")
else:
    print(a, "==", b, "is True" "\n")

if a!= b:
    print(a, "!=", b, "is True" "\n")
else:
    print(a, "!=", b, "is False" "\n")

if a > b:
    print(a, ">", b, "is True" "\n")
else:
    print(a, ">", b, "is False" "\n")

if a < b:
    print(a, "<", b, "is True" "\n")
else:
    print(a, "<", b, "is False" "\n")

if a >= b:
    print(a, ">=", b, "is True" "\n")
else:
    print(a, ">=", b, "is False" "\n")

if a <= b:
    print(a, "<=", b, "is True" "\n")
else:
    print(a, "<=", b, "is False" "\n")



""" 4. Logical Operators
    Below are the Logical Operators in python
    and
    or
    not
"""

a = 150
b = 100
c = 200
Logical_Operators = """ Logical Operators are used to combine conditional statements and they return a boolean value."""
print(Logical_Operators, "\n") # prints the variable
if a > b and a < c:
    print(a, "is greater than", b, "and less than", c, "\n") # comparinG greater than and less than condition usiong the 'and' operator
else:
    print(a, "is not greater than", b, "or less than", c, "\n") # if the condition is not met, it prints this statement

if a > b or a < c:
    print(a, "is greater than", b, "or less than ", c,"\n") # comparinG greater than and less than condition usiong the 'or' operator
else:
    print(a, "is not greater than", b, "or less than", c, "\n") # if the condition is not met, it prints this statement

if not a > b:
    print(a, "is not greater than", b, "\n") # using the 'not' operator to check if a is not greater than b
else:
    print(a, "is greater than", b, "\n")

""" 5. Identity Operators
    Below are the Identity Operators in python
    is
    is not
"""
Identity_Operators = """ 
Identity Operators are used to check if two variables are the same object and they return a boolean value."""

print(Identity_Operators, "\n") # prints the variable

a = 15
b = 10
if a is b:
    print(a, "is", b, "\n") # checks if a is b
else:
    print(a, "is not", b, "\n")

if a is not b:
    print(a, "is not", b, "\n") # checks if a is not b
else:
    print(a, "is", b, "\n")

""" 6. Membership Operators
    Below are the Membership Operators in python
    in
    not in
"""
Membership_Operators = """ Membership Operators are used to check if a value is present in a sequence (like a list, tuple, or string) and they return a boolean value."""

print(Membership_Operators, "\n") # prints the variable
my_list = [1, 2, 3, 4, 5] 
a = 3
b = 6
if a in my_list:
    print(a, "is in the list", my_list, "\n") # checks if a is in the list
else:
    print(a, "is not in the list", my_list, "\n")

if b not in my_list:
    print(b, "is not in the list", my_list, "\n") # checks if b is not in the list
else:
    print(b, "is in the list", my_list, "\n")


""" 7. Bitwise Operators
    Below are the Bitwise Operators in python
    &
    |
    ^
    ~
    <<
    >>
"""
Bitwise_Operators = """
Bitwise Operators are used to perform bit-level operations on integers and they return an integer value."""

print(Bitwise_Operators, "\n") # prints the variable
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print("a =", a, "b =", b, "\n")
print("a & b =", a & b)  # Bitwise AND
print("a | b =", a | b)  # Bitwise OR
print("a ^ b =", a ^ b)  # Bitwise XOR
print("~a =", ~a)  # Bitwise NOT
print("a << 1 =", a << 1)  # Bitwise Left Shift
print("a >> 1 =", a >> 1)  # Bitwise Right Shift

""" 8. Operator Precedence
Operator precedence determines the order in which operators are evaluated in an expression.
The precedence of operators in Python is as follows (from highest to lowest):
1. Parentheses `()`
2. Exponentiation `**`
3. Unary plus and minus `+`, `-`
4. Multiplication, Division, Floor Division, Modulus `*`, `/`, `//`, `%`
5. Addition and Subtraction `+`, `-`
6. Bitwise Shift Operators `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison Operators `==`, `!=`, `<`, `<=`, `>`, `>=`
11. Assignment Operators `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`, `&=`, `|=`, `^=`, `<<=`, `>>=`
12. Logical Operators `and`, `or`, `not`
"""
Operator_Precedence = """
Operator Precedence determines the order in which operators are evaluated in an expression.
The precedence of operators in Python is as follows (from highest to lowest):
"""
print(Operator_Precedence, "\n")  # prints the variable

# Example of operator precedence
x = 10
y = 5
z = 2
result = x + y * z  # Multiplication has higher precedence than addition
print("Result of x + y * z is:", result)  # Output: 20, because y * z is evaluated first
# Example of parentheses changing precedence
result_with_parentheses = (x + y) * z  # Parentheses change the order of evaluation
print("Result of (x + y) * z is:", result_with_parentheses)  # Output: 30, because addition is evaluated first
# Example of exponentiation precedence
result_exponentiation = x ** y + z  # Exponentiation has higher precedence than addition

print("Result of x ** y + z is:", result_exponentiation)  # Output: 1025, because x ** y is evaluated first