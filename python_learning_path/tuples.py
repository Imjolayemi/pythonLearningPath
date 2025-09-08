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

tupleConstructor = """You can also create a tuple using the tuple() constructor"""
print(tupleConstructor, "\n")

tupleUsingConstructor = tuple(("No", 240, "Agip Area", "Station Road", "Ede", "Osun State", "Nigeria"))

print("This tuple was created using the tuple() constructor \n \t:", tupleUsingConstructor, "\n")

accessingTuple = """ Accessing tuple items can be done using indexing and slicing"""
print(accessingTuple, "\n")
print("Accessing the first item in the Tuple below: \n \t", myTuple, " will give us \n \t:", myTuple[0], " \n by refering to the first index number")

print("Accessing the last item in the Tuple below: \n \t", myTuple, " will give us \n \t:", myTuple[-1], " \n by refering to the last index number using negative indexing \n ")

rangeOfItems = """You can also access a range of items in a tuple by using the slicing syntax"""
print(rangeOfItems, "\n")

print("Accessing items from index 1 to index 4 in the Tuple below: \n \t", myTuple, " will give us \n \t:", myTuple[1:5], "\n by refering to the index numbers in the slicing syntax \n ")

print("Accessing items from the index 2 to the end in the Tuple below: \n \t", myTuple, " will give us \n \t:", myTuple[2:], "\n by refering to the starting index number in the slicing syntax \n ")


checkingItem = """You can check if an item exists in a tuple by using the 'in' keyword"""
print(checkingItem, "\n")

if "Akure" in myTuple:
    print("This output is from checking if 'Akure' exists in the Tuple below \n \t:", myTuple, "\n \t: Yes, 'Akure' is in the tuple \n ")