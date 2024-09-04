# Class Activities (Lecture 2)

## Some examples about input("some message"), int(), and int(input())
# input("some message"):
classname = input("What is this class? ")
print("This class is ", classname)

# int()
num_5 = int('5') # convert '5' to 5
num_6 = int('6') # convert '6' to 6
total_num = num_5 + num_6 # calculate the sum
print("The total number is: ", total_num)

# int(input()): convert user input number into an integer number
user_input_number = int(input("Please type in a whole number: "))
print(user_input_number)


## TODO: Below are in-class exercise for Lecture 2
'''
1: Create a variable called number_of_units and assign 3 to it
    Then in the next line, print out number_of_units
'''
number_of_units = 3
print(number_of_units)


'''
2: What's wrong with the following lines of code? can you fix it?
print out the student's name by using its variable
'''
secondStudent = "Jane" # uncomment the code to see what's happened?
print(secondStudent)


'''
3. The code below calculates the area of a triangle. Add comments to 
each line explaining what it is doing.
'''
base = 10 # create variable base and then assign 10 to it
height = 3 # create variable height and then assign 3 to it
area = base * height # create a variable area and assign the result of base times height (expression) to it
area = area/2 # divide the value of variable area by 2 and then assign the result back to variable area
print("The triangle area is", area) # print out the value of area and put it in a sentence
