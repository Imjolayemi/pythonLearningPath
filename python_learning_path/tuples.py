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

updateTuple= """ Tuples are immutable, meaning you cannot change, add or remove items after the tuple has been created, but can be converted to a list and changed, then converted back to a tuple"""
print(updateTuple, "\n")

print("The original tuple is \n \t:", myTuple, "\n") # printing the original tuple

myList = list(myTuple) # converting tuple to list
myList[1] = 240 # changing the second item in the list
myTuple = tuple(myList) # converting the list back to a tuple

print("The updated tuple is \n \t:", myTuple, "\n") # printing the updated tuple

addingItems = """ You cannot add items to a tuple, but you can convert it to a list, add the item, then convert it back to a tuple"""
print(addingItems, "\n")

print("The original tuple is \n \t:", myTuple, "\n") # printing the original tuple

myList = list(myTuple) # converting tuple to list
myList.append("Africa") # adding an item to the list
myTuple = tuple(myList) # converting the list back to a tuple

print("The updated tuple is \n \t:", myTuple, "\n Adding 'Africa' to the tuple \n") # printing the updated tuple

removingItems = """ You cannot remove items from a tuple, but you can convert it to a list, remove the item, then convert it back to a tuple"""
print(removingItems, "\n")

print("The original tuple is \n \t:", myTuple, "\n") # printing the original tuple
myList = list(myTuple) # converting tuple to list
myList.remove("layout") # removing an item from the list
myTuple = tuple(myList) # converting the list back to a tuple

print("The updated tuple is \n \t:", myTuple, "\n Removing 'layout' from the tuple \n") # printing the updated tuple

unpackingTuple = """ In python you can unpack a tuple by assigning the items to different variables"""
print(unpackingTuple, "\n")

fruits = ("Mango", "Banana", "Orange") # creating a tuple
print("The original tuple is \n \t:", fruits, "\n") # printing the original tuple

(green, yellow, orange) = fruits # unpacking the tuple
print("The unpacked items are \n \t:", green, ",", yellow, "and", orange, "\n By giving each of them variable names") # printing the unpacked items

""" Unpacking items in a tuple can also be done using asterisk to assign the remaining items to a variable"""

fruits = ("Mango", "Banana", "Orange", "Pineapple", "Papaya") # creating a tuple
print("The original tuple is \n \t:", fruits, "\n") # printing the original tuple
(green, yellow, *tropic) = fruits # unpacking the tuple
print("The unpacked items are \n \t:", green, ",", yellow, "and", tropic, "\n By giving each of them variable names and using asterisk to assign the remaining items to a variable called tropic") # printing the unpacked items

tupleLoop = """ You can loop through tuples by using for loop and the while loop, using the len() function to know the length of tuple and range() function to loop through the index numbers"""
print(tupleLoop, "\n")

print("Looping through the tuple below using a for loop \n \t:", myTuple, "\n") #  printing out the tuple

for i in myTuple: # looping through the tuple using for loop
    print(i) # printing each item in the tuple

# looping through the tuple item by printing out an item using its index number
print("\nLooping through the tuple below by referring to the index number using for loop \n \t:", myTuple, "\n") #  printing out the tuple

for i in range(len(myTuple)): # looping through the tuple using the index number
    print(myTuple[i]) # printing each item in the tuple by refering to its index number

# looping through the tuple using while loop
print("\nLooping through the tuple below using while loop \n \t:", myTuple, "\n") #  printing out the tuple
i = 0 # initializing the index number
while i < len(myTuple): # looping through the tuple using while loop
    print(myTuple[i]) # printing each item in the tuple by refering to its index number
    i = i + 1 # incrementing the index number

joiningTuples = """ You can join two or more tuples by using the + operator and you can also multiply tuples by using the * operator """
print(joiningTuples, "\n")

tuple1 = ("a", "b", "c") # creating the first tuple
tuple2 = (1, 2, 3) # creating the second tuple
tuple3 = tuple1 + tuple2 # joining the two tuples
print("Joining two tuples by adding\n \t:", tuple1, " and ", tuple2, " using the + operator will give us \n \t:", tuple3, "\n") # printing the joined tuple

tuple4 = tuple3 * 2 # multiplying the joined tuple
print("Multiplying the joined tuple using * operator \n \t:", tuple3, " will give us \n \t:", tuple4, "\n") # printing the multiplied tuple