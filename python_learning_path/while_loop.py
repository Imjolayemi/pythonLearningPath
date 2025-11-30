""" While loop is used to execute a block of code repeatedly as long as a given condition is true.
    The condition is evaluated before executing the block of code.
    If the condition is true, the block of code is executed.
    This process continues until the condition becomes false.
    """
print(__doc__)

count = 0
while count < 5:
    print("Count is:", count)  # output: Count is: 0, Count is: 1, Count is: 2, Count is: 3, Count is: 4
    count += 1

""" We can also use else statement with while loop.
    The else block is executed when the condition becomes false.
    """
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Count has reached 5.")  # output: Count has reached 5.

""" We can use break statement to exit the while loop prematurely.
    When break statement is encountered, the loop is terminated and the control is transferred to the statement following the loop.
    """
count = 0
while count < 10:
    print("Count is:", count)
    if count == 5:
        print("Breaking the loop as count reached 5.")
        break  # output: Breaking the loop as count reached 5.
    count += 1

""" We can use continue statement to skip the current iteration of the loop and move to the next iteration.
    """
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count 3.")
        continue  # output: Skipping count 3.
    print("Count is:", count)  # output: Count is: 1, Count is: 2, Count is: 4, Count is: 5


""" We can use nested while loops to perform more complex tasks.
    """

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")  # output: i: 1, j: 1; i: 1, j: 2; i: 2, j: 1; i: 2, j: 2; i: 3, j: 1; i: 3, j: 2
        j += 1
    i += 1

    