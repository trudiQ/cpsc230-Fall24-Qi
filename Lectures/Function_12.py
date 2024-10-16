# Class Activities (Lecture 12)
import random

# example: generate a random number between 0 and 9 (inclusive)
x = random.randint(0, 9)
print(x, "is a random number between 0 and 9, inclusive")


'''
0. randint(a, b) is a function from a built-in library named random (see above import random)
that can be used to generate a random integer, N, between two integers (inclusive), a and b, where a <= N <= b.
PART 1: Define a function, named random_sum, that takes two input parameters, a and b (a < b),
    and generates two random numbers between a and b and return their sum.
PART 2: Invoke (use) the function to calculate the sum of two random numbers between 1 and 100 (inclusive)
and print the result.
'''
print("QUESTION 0 ---------------")
# write your code below
# PART 1: define a function of two input parameters: a, b
def random_sum(a, b):
    # generate the first random number 
    first = random.randint(a = a, b = b)
    # generate the second random number
    second = random.randint(a = a, b = b)
    # sum
    sum = first + second

    print("First is", first, ", Second is", second)

    return sum # this should always be your last line in the function definition

# PART 2: use the function by giving the arguments for a and b: 1 and 100
result = random_sum(a = 1, b = 100)
print("The sum is", result)


'''
1. Ask the user for their name, and print a welcome message to the user, e.g., "Welcome, [name]!"
    PART 1: Define a function with one input parameter, name, that prints a welcome message using that parameter.
    PART 2: Ask the user for their name, invoke (use) the function and input that name to the function as an argument.
Hint: 
- The function has no return statement.
'''
print("QUESTION 1 ---------------")
# PART 1: define the function
def greeting_user(name):
    print("Welcome,", name, "!")

# PART 2: use the function
user_name = input("What's your name? ")
greeting_user(name = user_name)


'''
2. PART 1: Define a function that calculate a rectangle's perimeter based on
   input parameters: length and width. Return the calculated perimeter as output.
        Hint: rectangle's perimeter is 2 * (length + width). 
   PART 2: Invoke (use) the function you just defined to calculate the perimeter 
   of a rectangle of length 5 and width 3 and print the result.
'''
print("QUESTION 2 ---------------")
# PART 1: define the function
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# PART 2: use the function
my_perimeter = calculate_perimeter(length=5, width=3)
print("The perimeter of the rectangle is", my_perimeter)

'''
3. PART 1: Define a function that returns True if the input parameter, number, is greater than 10,
    and returns False otherwise.
   PART 2: Use the function's return as part of if/else to check 
    the input argument of 16 and print out:
     "[argument] is greater than 10" or "[argument] is not greater than 10"
'''
print("QUESTION 3 ---------------")
# PART 1: define the function
## Solution 1:
def is_greater(number):
    result = False # create a variable (and assign an arbitrary value to it) to hold the output of this function
    if number > 10:
        result = True
    else:
        result = False
    return result

## Solution 2:
def is_greater_sol2(number):
    # typically, a function should have one return statement;
    # in this case, since it's part of is/else, only one return statement will be activated each time
    if number > 10:
        return True
    else:
        return False

# PART 2: envoke the function
my_number = 16 # given argument
result = is_greater(number=my_number)
if result == True:
    print(my_number, "is greater than 10")
else:
    print(my_number, "is not greater than 10")

