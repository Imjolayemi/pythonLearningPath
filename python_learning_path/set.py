defSet = """ Set in python
# A set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
# They are unordered, meaning that the items have no defined order, and you cannot refer to an item by index or key.
# They are unchangeable, meaning that you cannot change the items after the set has been created.
# They are unindexed, meaning that the items have no defined order, and you cannot refer to an item by index or key.
# Sets are written with curly brackets.
# Sets are used to store multiple items in a single variable. 
# Set does not accept duplicate values, where two or more items have the same value they are considered as one value
# In set True and 1 are considered the same value, likewise False and 0 are considered the same value."""
print(defSet, "\n")

myset = {"lion", "goat", "crocodile"} # Creating a set
myset2 = {1,2,3}
myset3 = {True, False}
print("An Example of a set is shown below \n \t:", myset, "\n") # Output: {'goat', 'crocodile', 'lion'}
print(type(myset), "\n")

setlength = """ Finding the length of a set can be done using the len() function """
print(setlength, "\n")

print("Length of myset \n \t :", myset, "is \n \t :", len(myset), "\n")

setConstructor = """ set can also be created using constructor which is set() function """
print(setConstructor , "\n")

myset4 = set(("ominvore", "herbivore", "carnivore")) # note the double round brackets
print("An Example of a set created using constructor is shown below \n \t:", myset4, "\n") # Output: {'herbivore', 'carnivore', 'ominvore'}

accessSet = """ You cannot access items in a set by referring to an index or a key. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword. """
print(accessSet, "\n")

y = 0
for x in myset:
    y += 1
    print("The item at index", y, "is \n \t:", x, "\n")

print("Is lion present in myset ? \n \t:", "lion" in myset, "\n") # Output: True
print("Is tiger present in myset ? \n \t:", "tiger" in myset, "\n") # Output: False

addSet = """ To add one item to a set use the add() method. To add more than one item to a set use the update() method. """
print(addSet, "\n")

myset.add("tiger")
print("Adding an item(tiger) to myset using add() method \n \t:", myset, "\n") # Output: {'goat', 'crocodile', 'lion', 'tiger'}

setlist = ["elephant", "deer", "monkey"]
print("A list named setlist is created \n \t:", setlist, "\n")
myset.update(setlist)

print("Adding multiple items(elephant, deer, monkey) to myset using update() method \n \t:", myset, "\n") # Output: {'goat', 'crocodile', 'lion', 'tiger', 'elephant', 'deer', 'monkey'}

removeSet = """ To remove an item in a set, use the remove(), or the discard() method. The only difference between remove() and discard() is that remove() will raise an error if the specified item does not exist, and discard() will not. """
print(removeSet, "\n")

myset.remove("crocodile")
print("Removing an item(crocodile) from myset using remove() method \n \t:", myset, "\n") # Output: {'goat', 'lion', 'tiger', 'elephant', 'deer', 'monkey'}

myset.discard("crocodile") # does not raise an error
print("Removing an item(crocodile) from myset using discard() method \n \t:", myset, "\n") # Output: {'goat', 'lion', 'tiger', 'elephant', 'deer', 'monkey'}

x = myset.pop() # removes a random item
print("Removing a random item(", x, ") from myset using pop() method \n \t:", myset, "\n") # Output: {'goat', 'lion', 'tiger', 'elephant', 'deer', 'monkey'}

clearSet = """ To clear the set, use the clear() method. """
print(clearSet, "\n")

myset3.clear()
print("Clearing all items from myset3 using clear() method gives empty set \n \t:", myset3, "\n") # Output: set()

delSet = """ You can also delete the set completely using the del keyword. """
print(delSet, "\n")

del myset3
print("myset3 has been deleted completely using the del keywork \n \t:")

joinSet = """ There are several ways to join two or more sets in Python. You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another. """
print(joinSet, "\n")

setA = {"a", "b", "c"}
setB = {1, 2, 3} 
print("Two sets named setA and setB are created \n \t:", setA, "and", setB, "\n")
setC = setA.union(setB)
print("Joining two sets setA and setB using union() method gives a new setC \n \t:", setC, "\n") # Output: {'a', 1, 2, 3, 'c', 'b'}
setA.update(setB)
print("Joining two sets setA and setB using update() method updates setA \n \t:", setA, "\n") # Output: {'a', 1, 2, 3, 'c', 'b'}

print("You can also join two sets using the | operator by creating a new setC = setA | setB which gives the same result as union() method but can only works for sets not for other iterables,which result to the answer below \n \t:", setC, "\n")

intersectSet = """ The intersection_update() method will keep only the items that are present in both sets upon updating the original set. The intersection() method will return a new set, that only contains the items that are present in both sets. """
print(intersectSet, "\n")

setD = {"apple", "pineapple", "mango"}
setE = {"mango", "banana", "cherry"}
print("Two sets named setD and setE are created \n \t:", setD, "and", setE, "\n")
setF = setD.intersection(setE)
print("Finding the intersection of two sets setD and setE using intersection() method gives a new setF \n \t:", setF, "\n") # Output: {'mango'}

setD.intersection_update(setE)
print("Finding the intersection of two sets setD and setE using intersection_update() method updates setD to \n \t:", setD, "\n") # Output: {'mango'}

print("You can also find the intersection of two sets using the & operator by creating a new setF = setD & setE which gives the same result as intersection() method but can only works for sets not for other iterables,which result to the answer below \n \t:", setF, "\n")

diffSet = """ The difference_update() method will remove the items that are present in both sets from the original set. The difference() method will return a new set, that contains only the items that are not present in both sets. """
print(diffSet, "\n")

setG = {"apple", "pineapple", "mango"}
setH = {"mango", "banana", "cherry"}
print("Two sets named setG and setH are created \n \t:", setG, "and", setH, "\n \t setG has mango in it which is also present in setH, which will be removed from setG when difference or difference_update method is used to  give the answers below")
setI = setG.difference(setH)
print("\t:", setI, "\n") # Output: {'apple', 'pineapple'}

setG.difference_update(setH)
print("Finding the difference of two sets setG and setH using difference_update() method updates setG to \n \t:", setG, "\n") # Output: {'apple', 'pineapple'}

print("You can also find the difference of two sets using the - operator by creating a new setI = setG - setH which gives the same result as difference() method but can only works for sets not for other iterables,which result to the answer below \n \t:", setI, "\n")

symDiffSet = """ The symmetric_difference_update() method will keep only the elements that are NOT present in both sets upon updating the original set. The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets. """
print(symDiffSet, "\n")

setJ = {"apple", "pineapple", "mango"}
setK = {"mango", "banana", "cherry"}
print("Two sets named setJ and setK are created \n \t:", setJ, "and", setK, "\n \t setJ has mango in it which is also present in setK, which will be removed from both sets when symmetric_difference or symmetric_difference_update method is used to  give the answers below")
setL = setJ.symmetric_difference(setK)
print("\t:", setL, "\n") # Output: {'apple', 'pineapple', 'banana', 'cherry'}

setJ.symmetric_difference_update(setK)
print("Finding the symmetric difference of two sets setJ and setK using symmetric_difference_update() method updates setJ to \n \t:", setJ, "\n") # Output: {'apple', 'pineapple', 'banana', 'cherry'}

print("You can also find the symmetric difference of two sets using the ^ operator by creating a new setL = setJ ^ setK which gives the same result as symmetric_difference() method but can only works for sets not for other iterables,which result to the answer below \n \t:", setL, "\n")

