""" For loop in python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects."""
print(__doc__)

# Example of for loop iterating over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # output: apple, banana, cherry

# Example of for loop iterating over a string
for char in "hello":
    print(char)  # output: h, e, l, l, o

# Example of for loop with range()
for i in range(5):
    print(i)  # output: 0, 1, 2, 3, 4

""" We can also use else statement with for loop.
    The else block is executed when the loop has iterated over all items.
    """
for i in range(3):
    print(i)  # output: 0, 1, 2
else:
    print("Loop has completed.")  # output: Loop has completed.

""" We can use break statement to exit the for loop prematurely.
    When break statement is encountered, the loop is terminated and the control is transferred to the statement following the loop.
    """
for i in range(10):
    if i == 5:
        break
    print(i)  # output: 0, 1, 2, 3, 4

""" We can use continue statement to skip the current iteration of the loop and move to the next iteration.
    """
for i in range(5):
    if i == 3:
        continue
    print(i)  # output: 0, 1, 2, 4

""" We can use nested for loops to perform more complex tasks.
    """
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")  # output: i: 1, j: 1; i: 1, j: 2; i: 2, j: 1; i: 2, j: 2; i: 3, j: 1; i: 3, j: 2

""" we also have the pass statement in for loops.
    The pass statement is a null operation; it does nothing when executed.
    It is used as a placeholder in loops or functions where code will eventually go.
    """
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    print(i)  # output: 0, 1, 2, 3, 4



    

    