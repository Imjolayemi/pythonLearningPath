dictionary = """ Dictionaries in Python are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values. """
print(dictionary, "\n")

mydict = { 
    "name": "jolayemi",
    "age": 17,
    "country": "Nigeria",
    "hobby": ["coding", "eating", "movie"]
}
print(mydict, "\n The length of the above dictionary is ", len(mydict), "\n While the the type is ", type(mydict), "\n")

# Accessing items in a dictionary
print("Accessing items in a dictionary")
print("The name in the dictionary is ", mydict["name"]) #print out the value of the key name

# we can also use the get() method to access values
print("The age in the dictionary is ", mydict.get("age"), " using the get() method\n")

dictkeys = """ Key values in a dictionary are used to access the values associated with them. We can use the key() function to get a list of all the keys in the dictionary. """
print(dictkeys, "\n")
print("The keys in the dictionary are ", mydict.keys(), "\n")

dictvalues = """ The values in dictionary can be access using the values() function to get a list of all values in the dictionary"""
print(dictvalues, "\n")

print("The values in the dictionary are ", mydict.values(), "\n")

dictItems = """ The items in dictionary can be access using the items() function to get a list of all items in the dictionary"""
print(dictItems, "\n")

print("The items in the dictionary are ", mydict.items(), "\n") # the items in the dictionary will be the output

checkKey = """ To check if a key exists in a dictionary, we can use the 'if' and 'in' keyword. """
print(checkKey, "\n")

if "country" in mydict:
    print("Yes, 'country' is one of the keys in the dictionary, which we use the 'if' and 'in' keywords to get them.\n")

changeValue = """ To change the value of a specific item in a dictionary, we can refer to its key name. """
print(changeValue, "\n")

mydict["age"] = 18
print("The age value has been changed to ", mydict["age"], "\n")

updateDict = """ We can also use the update() method to change the value of a specific item in a dictionary. """  
print(updateDict, "\n")

mydict.update({"hobby": ["reading", "traveling"]})
print("The hobby value has been changed to ", mydict["hobby"], "\n")

addItem = """ To add an item to a dictionary, we can use a new key and assign a value to it. """
print(addItem, "\n")
mydict["favorite_color"] = "blue"
print("The new item added to the dictionary is favorite_color: ", mydict["favorite_color"], "\n")

