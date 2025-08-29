"""Tuples in python are immutable, ordered and unchangeable collections of items. 
They allow duplicate values.
"""
# Creating a tuple
myTuple = ("No", 58, "odopo", "layout", "ijoka", "Akure", "Ondo State", "Nigeria")
print(myTuple, "\n")

"""tuple length can also be determined using the len() function"""
print("The length of my tuple is \n \t:", len(myTuple), "\n")

"""You can also create a tuple with one item by adding a comma after the item"""
oneItemTuple = ("Akure",)
print("This tuple is a one item tuple \n \t:", oneItemTuple, "\n")

# tuple can also be of different data types
differentDataTypeTuple = ("Akure", 58, True, 5.8)
print("This tuple has different data types \n \t:", differentDataTypeTuple, "\n")

""" in python tuple is also recognized as a data type of its own,"""
print("The data type of myTuple is \n \t:", type(myTuple), "\n")
print("The data type of oneItemTuple is \n \t:", type(oneItemTuple), "\n")