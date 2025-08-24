"""
list in python is a collection of items that are orrdered, changeable and allow duplicate values.

lists are defined by having values between square barects [].

lists can contain any data types 
and can be nested, meaning a list can contain other lists as elements.

list can also be constyructed using the list() constructor.

list also as a type in python, which can be checked using the type() functiion.
"""

myList = list() # using the list constructor
list1 = ["apple", "banana", "cherry", "watermelon", "pineapple", "orange", "grape"] # using square brackets
list2 = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 22, 24,] # list of integers
list3 = [True, False, True] # list of boolean values

print("\n myList:", myList, "\t Type of myList:", type(myList), "\n")  # prints the empty list and the type of myList

print("list1:", list1, "\t Type of list1:", type(list1), "\n")  # prints the list of strings and the type of list1

print("list2:", list2, "\t Type of list2:", type(list2), "\n")  # prints the list of integers

print("list3:", list3, "\t Type of list3:", type(list3), "\n")  # prints the list of boolean values

# Lists can also be nested
nested_list = [list1, list2, list3]  # a list containing other lists
print("nested_list:", nested_list, "\t Type of nested_list:", type(nested_list), "\n")  # prints the nested list and its type

print(len(myList), "is the length of myList \n")  # prints the length of the empty list

print(len(list1), "is the length of list1 \n")  # prints the length of list1

print(len(list2), "is the length of list2 \n")  # prints the length of list2

print(len(list3), "is the length of list3 \n")  # prints the length of list3

print(len(nested_list), "is the length of nested_list \n")  # prints the length of the nested list

""" 
Accessing python list items by using index number
index number of a list always starts with 0, which means the first item in a list is at index 0 and the last item is at index -1.
Accessing list items can be done using square brackets [] and the index number of the item.
"""

print("Accessing list items by index number \n")  # prints the header for accessing list items by index number



print("First item in list1:", list1[0], "\n")  # prints the first item in list1

print("Second item in list1:", list1[1], "\n")  # prints the second item in list1

print("Last item in list1:", list1[-1], "\n")  # prints the last item in list1

print("First item in list2:", list2[0], "\n")  # prints the first item in list2

print("Second item in list2:", list2[1], "\n")  # prints the second item in list2

print("Last item in list2:", list2[-1], "\n")  # prints the last item in list2

print("The third item in list1 to the sixth item in list1:", list1[2:6], "\n")  # prints the third to sixth items in list1

print("The first five items in list2:", list2[:5], "\n")  # prints the first five items in list2

print("The last three items in list3:", list3[-3:], "\n")  # prints the last three items in list3

""" 
checking if an item exists in a list
This can be done using the 'in' operator, which returns True if the item exists in the list and False if it does not.
"""
print("Checking if an item exists in a list \n")  # prints the header for checking if an item exists in a list
if "apple" in list1:
    print("apple is in list1 \n")  # checks if "apple" is in list1
else:
    print("apple is not in list1 \n") # checks if "apple" is not in list1

if "mango" in list1:
    print("mango is in list1 \n")  # checks if "mango" is in list1
else:
    print("mango is not in list1 \n") # checks if "mango" is not in list1

if 10 in list2:
    print("10 is in list2 \n")  # checks if 10 is in list2
else:
    print("10 is not in list2 \n") # checks if 10 is not in list2

if 5 in list2:
    print("5 is in list2 \n")  # checks if 5 is in list2
else:
    print("5 is not in list2 \n") # checks if 5 is not in list2


even = [1, 2, 4, 6, 8, 9] # list of even numbers
even[1:5] = [3, 5, 7]  # replacing the second item and all 
print("even changed to odd", even, "\n")  # prints the modified list 

""" items  can also be inserted into a list using the insert() method.

The insert() method takes two arguments: the index at which to insert the item and the item to be inserted.
"""
even.insert(5,10) # inserting 10 at index 5
print("even after inserting 10 at index 5:", even, "\n")  # prints the modified list after inserting 10

"""we can also append items to a list using the append() method.
The append() method adds an item to the end of the list.
"""
even.append(12)  # appending 12 to the end of the list
print("even after appending 12 to the end of the list:", even, "\n")  # prints the modified list after appending 12

""" list can also be extended using the extend() method.
The extend() method takes an iterable (like a list or a tuple) and adds its items to the end of the list.
"""
even.extend([14, 16, 18])  # extending the list with more even numbers
print("even after extending with more even numbers:", even, "\n")  # prints the modified list after extending

""" we can also remove items from a list using the remove() method.
The remove() method takes the item to be removed as an argument and removes the first occurrence of that item from the list.
If the item is not found in the list, it raises a ValueError.
"""
even.remove(3)  # removing 10 from the list
print("even after removing 3:", even, "\n")  # prints the modified list after removing 3

""" we can also remove items from a list using the pop() method.
The pop() method removes the item at the specified index and returns it.
If no index is specified, it removes and returns the last item in the list.
"""
even.pop(1)  # removing the item at index 1 and 2
print("even after popping the item at index 1 and 2:", even, "\n")  # prints the modified list after 

""" we can delete items from a list using the del statement.
The del statement removes the item at the specified index.

We can also delete the entire list using the del statement.
if the index is not specified 
"""
del even[1] # deleting the item at index 1
print("even after deleting the item at index 1:", even, "\n")  # prints the modified list after deleting the item at index 1

del list3 # deleting the entire list3
print("NOTICE: list3 has been deleted \n")  # prints the message that list3 has been deleted

""" we can also clear a list using the clear() method.
The clear() method removes all items from the list, leaving it empty.
"""
even.clear()  # clearing the list
print("even after clearing the list:", even, "\n")  # prints the modified list after clearing it

""" looping through a list can be done using a for loop or a while loop."""
print("Looping through a list \n")  # prints the header for looping through a list
for item in list1:  # looping through list1
    print(item,"\n")  # prints each item in list1

for index, item in enumerate(list2):  # looping through list2 with index
    print(f"Index {index}: {item} \n")  # prints each item in list2 with its index

i = 0 # initializing the index variable
while i < len(list1):  # looping through list1 using a while loop
    print(f"Item at index {i}: {list1[i]} \n")  # prints each item in list1 with its index
    i += 1  # incrementing the index variable

# printing the items in a list using it index number to loop through the list
print("Printing items in a list using index number \n")  # prints the header for printing items in a list using index number

for i in range(len(list1)):  # looping through list1 using its index number
    print("Item at index", i, ":", list1[i], "\n")  # prints each item in list1 with its index

# you can also print out the items in a list using list comprehension
print("Printing items in a list using list comprehension \n")  # prints the header for printing items in a list using list comprehension

print("List1 items using list comprehension:")  # prints each item in list1 using list comprehension
[print(item,"\n") for item in list1]  # prints each item in list1

# you can also print new list using list comprehension
print(f"New list that has the letter \'a\' from \n\t {list1} \n using list comprehension:\n\t{[a_list for a_list in list1 if 'a' in a_list]}")  # prints a new list that has the letter 'a' from list1 using list comprehension

print(f"\n A new list that print the items from index 2 in \n\t {list1} \n to index 5 \n\t{[x for x in list1[2:6]]}")

print([x if x != "banana" else "fruit" for x in list1])  # prints a new list that replaces "banana" with "orange" in list1 using list comprehension


""" Sorting a list can be done using the sort() method."""

print("Sorting a list \n")  # prints the header for sorting a list
list2.sort()  # sorting list2 in ascending order
print("list2 after sorting in ascending order:", list2, "\n")  # prints the sorted list2

print("list1 before sorting in descending order:", list1, "\n")  # prints the sorted list1
list1.sort(reverse=True)  # sorting list1 in descending order
print("list1 after sorting in descending order:", list1, "\n")  # prints the sorted list1

list1.reverse()  # reversing the order of list1
print("list1 after reversing the order:", list1, "\n")  # prints the reversed list1

"""Sorting a list can also be done using the sorted() function.
The sorted() function returns a new"""
print("Sorting a list using the sorted() function \n")  # prints the header for sorting a list using the sorted() function
sorted_list2 = sorted(list2)  # sorting list2 in ascending order using the sorted() function
print("sorted_list2 after sorting in ascending order using the sorted() function:", sorted_list2, "\n")  # prints the sorted list2

""" we can copy a list using the copy() method."""
print("Copying a list using the copy() method \n")  # prints the header for copying a list using the copy() method
list1_copy = list1.copy()  # copying list1 using the copy() method
print("list1_copy after copying list1:", list1_copy, "\n")  # prints the copied list1

""" we can also copy a list using the list() constructor."""
print("Copying a list using the list() constructor \n")  # prints the header for copying a list using the list() constructor
list2_copy = list(list2)  # copying list2 using the list() constructor
print("list2_copy after copying list2 using the list() constructor:", list2_copy, "\n")  # prints the copied list2

""" we can also copy a list using slicing."""
print("Copying a list using slicing \n")  # prints the header for copying a list using slicing
list3_copy = list3[:]  # copying list3 using slicing
print("list3_copy after copying list3 using slicing:", list3_copy, "\n")  # prints the copied list3

