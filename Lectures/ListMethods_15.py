# Class Activities (Lecture 15)

# Outline
# 1 - 2 Exercise questions list operations
# 3 - 4 Exercise question on list methods
# 5 Exercise questions on list functions
# 5.B Exercise questions on using for-loops on lists
# 6 - 7 More practice questions on list methods and functions

## List operations 
'''
1. List concatenation with +
TODO: Create a new list ['a','b','c','d','e','f'] 
        using the lists below
'''
print("QUESTION 1: ")
list0 = ['a', 'b', 'c']
list1 = ['d', 'e', 'f']

list_concatenate = list0 + list1
print(list_concatenate)

'''
2. List repetition with *
TODO: Repeat the list below 3 times
        you should see [1, 2, 3, 1, 2, 3, 1, 2, 3]
'''
print("QUESTION 2: ")
list2 = [1, 2, 3]

list_repeat = list2 * 3
print(list_repeat)


## List methods
'''
3. Given a list below representing a to-do list, 
    a) Use append() to add "Go for a walk" to the end of the list
    b) Use insert() to add "Buy groceries" as the SECOND item in the list
    c) Use pop() to remove AND print the LAST task in the list
    d) Use remove() to remove "Read a book" from the list
    e) Use sort() to sort the list alphabetically AND print the sorted list
'''
print("QUESTION 3: ")
tasks = ["Complete homework", "Read a book", "Write a report"]
# write your code below
# a) 
tasks.append("Go for a walk")
print(tasks)
# b)
tasks.insert(1, "Buy croceries")
print(tasks)
# c)
last_task = tasks.pop(-1)
print(last_task)
# d)
tasks.remove("Read a book")
# e)
tasks.sort()
print(tasks)




'''
4. Given a list of colors below,
    a) Use count() to find and print how many times "red" appears in the list.
    b) Use index() to find and print the position of the FIRST "blue" in the list.
    c) Using a for-loop, find and print the indices of all occurrences of "red" in the list.
    d) Use count() to check if "yellow" in the list. 
        If yes, print its position; if no, print a message saying "Yellow is not in the list".
'''
print("QUESTION 4: ")
colors = ["red", "blue", "green", "red", "blue", "red"]
# write your code below
# a)
count_red = colors.count("red")
print(count_red)
# b)
index_blue = colors.index("blue")
print(index_blue)
# c)
for i in range(0, len(colors), 1): # range() creates a sequence of indices: 0,1,2,3,4,5
    if colors[i] == "red": # access each item in colors using its index
        print("The index of red is", i)
# d)
if colors.count("yellow") > 0:
    print(colors.index("yellow"))
else:
    print("Yellow is not in the list")

## List functions - you MUST USE LIST FUNCTIONS, not methods!
'''
5. Consider a list of temperatures (in Fahrenheit) for a week,
    a) Find and print the length of the temperatures list.
    b) Find and print the maximum and minimum temperatures of the week.
    c) Calculate and print the sum of the temperatures.
    d) Calculate and print the average temperature for the week using sum() and len().
    e) Sort and print the temperatures in ascending order.
    f) Sort and print temperatures in descending order.
'''
print("QUESTION 5: ")
temperatures = [72, 75, 68, 79, 71, 73, 78]
# write your code below
# a)
length = len(temperatures)
print(length)
# b)
min_temp = min(temperatures)
max_temp = max(temperatures)
print("min temperature is", min_temp, "; max temprature is", max_temp)
# c)
sum_temp = sum(temperatures)
print("sum of temperatures is", sum_temp)
# d)
avg_temp = sum_temp/length
print("average temperature is", avg_temp)
# e) 
temp_ascend = sorted(temperatures)
print("sort in ascending:", temp_ascend)
# f)
temp_descend = sorted(temperatures, reverse=True)
print("sort in descending:", temp_descend)



## More practice questions on for-loops on lists
'''
5.B Following Q5 above, 
    a) Instead of using sum(), can you use a for-loop to iterate all the numbers in temperature,
        and calculate the sum of those numbers?
        Compare your result in 5-c)
    b) Create an empty list, my_list, and use another for-loop to iterate all the items in temperature, and add all the items
        that are greater than 74 to my_list. Print my_list at the end.
    c) Use another for-loop and range() to iterate all the items in temperature, 
        and print the indices of all the items in temperatures that are greater than 74. You should see 1, 3, 6.
'''
print("QUESTION 5B: ")
# write your code below
# a)
sum = 0
for temp in temperatures:
    sum += temp
print(sum)

# b)
my_list = []
for temp in temperatures:
    if temp > 74:
        my_list.append(temp)
print(my_list)

# c)
for i in range(len(temperatures)):
    if temperatures[i] > 74:
        print(i)



# More practice questions on list methods and list functions

'''
6. Start with the following list of numbers:
    1) Use the append() method to add the number 5 to the list.
    2) Use the insert() method to insert 15 at the beginning of the list.
    3) Use the pop() method to remove and print the second number in the list.
    4) Use the remove() method to remove the number 7 from the list.
    5) Use the sort() method to sort the list in descending order and print the result.
'''
print("QUESTION 6: ")
numbers = [10, 3, 7, 2, 8]
# write your code below

'''
7. You work for an online marketplace, and you have collected customer review scores for a popular product:
    1) Calculate the total number of reviews.
    2) Find the highest and lowest review scores.
    3) Calculate the average review score.
    4) Sort and print the review scores in both ascending and descending order.
    5) The product manager decides to filter out the lowest score for a better understanding of the product's performance. 
        Remove the lowest score, recalculate the average, and print it.
'''
print("QUESTION 7: ")
reviews = [4.5, 3.8, 4.2, 4.7, 3.9, 4.0]
# write your code below







