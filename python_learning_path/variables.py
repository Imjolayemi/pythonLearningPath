"""
this module contains how to create variables in python

variables are used to store data values

variables are created when you assign a value to them
"""
a = 5  # integer
b = 2.5  # float 
c = "Hello"  # string

print(a)  # prints the value of a
print(b)  # prints the value of b
print(c)  # prints the value of c

# whereas a, b, c are variables, 5, 2.5, "Hello" are values

# variables can be reassigned to different values and types
d = 10  # integer
d = "reassigned"  # string

print(d)  # prints the value of d

""" Casting variables
Casting is the process of specifying the type of a variable
"""
x = int(5)  # x is an integer
y = float(5)  # y is a float
z = str(5)  # z is a string

# the type of a variable can be checked using the type() function

print(type(x))  # prints the type of x
print(type(y))  # prints the type of y
print(type(z))  # prints the type of z


"""
Assigning multiple values to multiple variables can be done in one line

Assigning multiple variables to a single value can be done in one line

Also unpacking a collection of values into multiple variables can be done in one line
"""
x, y, z = 1, 2, 3  # assigning multiple values to multiple variables
a = b = c = 4  # assigning multiple variables to a single value
fruit = ["apple", "banana", "cherry"]  # collection of values
d, e, f = fruit  # unpacking a collection of values into multiple variables

print(x, y, z)  # prints the values of x, y, z
print(a, b, c)  # prints the values of a, b, c
print(fruit)  # prints the collection of values
print(d + e, f)  # prints the values of d, e, f after unpacking


def myfunc():
    global g
    g = "This is a Global Variable created inside the myfunc()"


myfunc()  # calling the function to create the global variable
print(g)  # prints the value of g before calling the function

""""
casting variables

casting is the process of converting a variable from one type to another

casting is done using the int(), float(), str() functions
"""
n = int(3.14) # converting float to int
print("\nThe value of n changes from float to integer, where the value of n changes to",n) # prints the value of n after converting float to int


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print("\n",a)


