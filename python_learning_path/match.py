""" Match statemnt is used to perform difrrent actions based on different conditions.
    instead of using multiple if-elif-else statements, match statement can be used to make the code more readable.

    match is evaluated once and compared with each case.
    When a match is found, the corresponding block of code is executed.
    """
print(__doc__)

head = 1
match head:
    case 1:
        print("The Head of the family is Father. \n") # output: The Head of the family is Father.
    case 2:
        print("The Head of the family is Mother. \n") # output: The Head of the family is Mother.
    case 3:
        print("The Head of the family is Son. \n") # output: The Head of the family is Son.

""" We also have the default case in match statement which is represented by underscore(_)
    If none of the cases match, the default case is executed.
    """

head = 4
match head:
    case 1:
        print("The Head of the family is Father. \n")
    case 2:
        print("The Head of the family is Mother. \n")
    case 3:
        print("The Head of the family is Son. \n")
    case _:
        print("No match found. \n") # output: No match found.

""" We can also use multiple patterns in a single case using the pipe (|) operator.
    If any of the patterns match, the corresponding block of code is executed.
    """

head = 2
match head:
    case 1 | 2:
        print("The Head of the family is Parent. \n") # output: The Head of the family is Parent.
    case 3:
        print("The Head of the family is Son. \n") 
    case _:
        print("No match found. \n")

""" We can also use guards in match statement to add additional conditions to a case.
    A guard is an if statement that follows a case pattern.
    The block of code is executed only if the pattern matches and the guard condition is true.
    """
employment_status = True
head = 1
match head:
    case 1 if employment_status:
        print("The Head of the family is father. \n") # output: The Head of the family is father.
    case 1 if not employment_status:
        print("You have to find a job. \n") # output: You have to find a job.
    case _:
        print("No match found. \n") # output: No match found.

