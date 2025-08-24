""" 
This module contains string manipulation functions.
"""

a = "Hello, World!"  # string

# string is also arrays in python
print("The first character of", a, "is", a[0], "\n")  # H
print("The second character of", a, "is", a[1], "\n")  # e
print("The third character of", a, "is", a[2], "\n")  # l
print("The fourth character of", a, "is", a[3], "\n")  # l
print("The fifth character of", a, "is", a[4], "\n")  # 



#loops in strings 
b = a[2]  # l

for d in a:  # iterate through the string
    print(d,"\n")  # print each character in the string

# The length of  string can be found using the len() function
print("The length of", "\""+ a +"\"", "is", len(a), "\n")  # 13

#check string
if "Hello" in a:  # check if "Hello" is in the string
    print("Yes, 'Hello' is in", "\""+ a +"\"", "\n")  # Yes, 'Hello' is in Hello, World!

#check if not in string
if "hey" not in a:
    print("No, 'hey' is not in", "\""+ a +"\"", "\n")  # No, 'hey' is not in Hello, World!


# string slicing
print("The first 5 characters of", "\""+ a +"\"", "are", a[0:5], "\n")  # Hello

# Negative indexing
print("The last character of", "\""+ a +"\"", "is", a[-1], "\n")  # !
print("The last characters of", "\""+ a +"\"", "starting from o without including the last last character are", a[-5:-1], "\n") #orld


# modifying strings
# strings are immutable in python, so we cannot modify them directly

print(a.replace("Hello", "Hi"), "\n")  # Hi, World!
print(a.upper(), "\n")  # HELLO, WORLD!
print(a.lower(), "\n")  # hello, world!
print(a.strip(), "\n")  # Hello, World! (removes whitespace from the beginning and end of the string)

# string formatting in python f-string
age = 12 # an integer
txt = f"My name is john, and i am {age} years old" # f-string
print(txt,"\n")
dad_Age = 45  # an integer

txt1 = f"My name is john, and my dad is {dad_Age} years old, and the addition of my age and my dad's age is {age + dad_Age:.3f}."  # f-string

print(txt1, "\n")

#Escape characters in strings
print("Hello, World!\n")  # new line
print("Hello, World!\t")  # tab
print("Hello, World!\\")  # backslash
print("Hello, World!\'")  # single quote
print("Hello, World!\"")  # double quote
print("Hello, World!\a")  # bell/alert sound
print("Hello, World!\b")  # backspace
print("Hello, World!\f")  # form feed
print("Hello, World!\r")  # carriage return
print("Hello, World!\v")  # vertical tab
print("Hello, World!\ooo")  # octal value
# print("Hello, World!\xhh")  # hexadecimal value
# print("Hello, World!\N{name}")  # unicode character
