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

removeItem = """ 
To remove an item from a dictionary, we can use the pop() method or the del keyword.
The pop() method removes the item with the specified key name.
The del keyword removes the item with the specified key name as well.
We can also use the clear() method to empty the dictionary. 
The del keyword can also delete the dictionary completely. 
The popitem() method removes the last inserted item (in versions 3.7 and later). 
"""
print(removeItem, "\n")

mydict.pop("country") #remove the country item
print("The dictionary after removing the country item using pop(): ", mydict, "\n")

del mydict["favorite_color"] #remove the favorite_color item
print("The dictionary after removing the favorite_color item using del: ", mydict, "\n")

mydict.popitem() #remove the last inserted item
print("The dictionary after removing the last inserted item using popitem(): ", mydict, "\n")

mydict.clear() #clear the dictionary
print("The dictionary after clearing all items using clear(): ", mydict, "\n")

newdict = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "color": "red"
}#create a new dictionary
print("A new dictionary has been created: ", newdict, "\n")

loopInDict = """ We can loop through a dictionary using a for loop. We can loop through the keys, values, or items in the dictionary. 
The default is to loop through the keys. 
You can use the keys() method to loop through the keys.
The values() method to loop through the values
And the items() method to loop through the items."""
print(loopInDict, "\n")

for key in newdict:
    print("Key: ", key, "\n") #loop through keys and print them


for value in newdict.values():
    print("Value: ", value, "\n") #loop through values and print them

for item in newdict.items():
    print("Item: ", item, "\n") #loop through items and print them

for x,y in newdict.items():
    print(x, y, "\n") #loop through items and print key and value separately

copyDict = """ To copy a dictionary, we can use the copy() method or the dict() function. """
print(copyDict, "\n")

dictcopy1 = newdict.copy() #using copy() method
print("Dictionary copied using copy() method: ", dictcopy1, "\n")

dictcopy2 = dict(newdict) #using dict() function
print("Dictionary copied using dict() function: ", dictcopy2, "\n")

nestedDict = """ A nested dictionary is a dictionary that contains other dictionaries as its values. """
print(nestedDict, "\n")

ElectronicsStore = {
    "laptop": {
        "brand": "Dell",
        "model": "XPS 13",
        "price": 999.99
    },
    "smartphone": {
        "brand": "Apple",
        "model": "iPhone 13",
        "price": 799.99
    },
    "tablet": {
        "brand": "Samsung",
        "model": "Galaxy Tab S7",
        "price": 649.99
    }
} #create a nested dictionary
print("A nested dictionary representing an electronics store: ", ElectronicsStore, "\n")

print("Accessing the model of the laptop: ", ElectronicsStore["laptop"]["model"], "\n") #accessing a value in the nested dictionary
print("Accessing the price of the smartphone: ", ElectronicsStore["smartphone"]["price"], "\n") #accessing another value in the nested dictionary

nestedDictLoop = """ We can loop through a nested dictionary using a for loop. We can loop through the outer dictionary and then loop through the inner dictionaries. """
print(nestedDictLoop, "\n")

for category, items in ElectronicsStore.items():
    print("Category: ", category, "\n")

    for item, details in items.items():
        print("    ",item, ": ", details, "\n")
    

# End of dictionaries.py