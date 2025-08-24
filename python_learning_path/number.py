# Numbers in python

# 1. Integer
x = 5 # Integer 
y = 10e-5 # Float
z = 3j # Complex number

print(x, "and the data type of",  x, " is ", type(x)) # <class 'int'>
print(y, "and the data type of",  y, " is ", type(y)) # <class 'float'>
print(z, "and the data type of",  z, " is ", type(z)) # <class 'complex'>


a = complex(x) # Convert int to complex

print(a)
print(int(y)) # Convert float to int

print(float(x)) # Convert int to float


"""Random number generation"""
import random

d = random.randrange(1, 10) # Random number between 1 and 10
print(d)

