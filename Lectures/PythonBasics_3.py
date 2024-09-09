# Class Activities (Lecture 3)

# Numbers
'''
Create a variable x and assign a random integer (e.g., 5) to it and 
print it and its type in one statement
'''
x = 5
print(x, type(x))
print(x, "is of ", type(x))

'''
Create a variable y and assign a random float (e.g., 1.3) to it and 
print it and its type in one statement
'''
y = 1.3 
print(y, "is of ", type(y))

# strings
'''
Create a string consisting of all types of characters:
numbers, letters, symbols, and spaces.
Print out the string and its type.
'''
str_1 = "Today is Sep 9, 2024!"
print(str_1, type(str_1))

# List
'''
Create a list of 1, 2, 3, 4, 5
'''
list_0 = [1, 2, 3, 4, 5]

'''
Create a list consisting of a string, an integer, a float
and a list.
Print out the list and its type.
'''
list_1 = ['Today is', 2024, 9.9, [1, 2, 3]]
print(list_1, type(list_1))

# Dictionary
'''
Create a variable of dictionary, named cpsc230
- keys are 'Name', 'School', 'Credits'
- values are 'Computer Science I', 'Engineer', an integer of 3
- Print out the dictionary and its type.
'''
cpsc230 = {'Name':'Computer Science I', 'School':'Engineer', 'Credits': 3}
print(cpsc230, type(cpsc230))

# Set
'''
Create a set called my_set, consisting of 1, 2, 3, 4, 5, 5, 5, 6 
Print out my_set. Did it change at all? 
Explain why.
'''
set_1 = {1, 2, 3, 4, 5, 5, 5, 6}
print(set_1) # a set contains unique items; duplicates are removed automatically 

# Type conversions
'''
Create two variables, a and b, assigned with '1.3' and '5',
Convert the first variable into a float 
Convert the second variable into an integer
Sum them up and assign the result to another variable, c
Print out the value of c, and its type.
Explain why the result is that type.
'''
a = '1.3'
b = '5'
a = float(a) # convert a string of a float number into a float
b = int(b) # convert a string os an integer into an integer
c = a + b # sum of a float and an integer is a float
print(c, type(c)) # as float has higher precision
