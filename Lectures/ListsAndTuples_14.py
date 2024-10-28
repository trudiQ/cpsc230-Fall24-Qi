# Class Activities (Lecture 14)

## lists
'''
0. Access a list of lists.
'''
recipe_ingredients = [["cheese", "chicken", "tomato sauce", "basil", "breadcrumbs"],
["chickpeas", "cucumber", "tzatziki", "tomatoes", "onion"],
["hamburger", "bun", "ketchup", "lettuce", "pickles", "mayo"],
["white beans", "celery", "diced tomatoes", "shallots", "broth"]]

print("QUESTION 0: ")
# TODO: Get 'tzatziki' from recipe_ingredients using indices 
#          and store it to variable, ingredient. 
#           print the variable to check the result
item = recipe_ingredients[1][2]
print(item)

# Count the number of ingredients in the recipe in total. 
#   Print the total number to check your answer. (The total number is 21)
# Hint: Use len() to get the number of items in a list
#       Use for loop to iterate each sub-list to get the number of items and sum them up
# TODO: write your code below
total_number = 0
for list in recipe_ingredients:
    total_number += len(list) # len(list) is the number of items in a sub-list
print("total number of ingredients is", total_number)


# If one's allergic to gluten, how to replace "bun" with "gluten-free bun" in recipe_ingredients?
#   print recipe_ingredients to check your answer.
# TODO: write your code below
recipe_ingredients[2][1] = "gluten-free bun" # modify the 2nd item in the 3rd sublist - "bun"
print(recipe_ingredients[2])


'''
1. Read and run the code below. Turn this while loop into a for loop.
    To check your answer, use ''' ''' to comment out the while loop (DO NOT comment my_list)
'''
print("QUESTION 1: ")
my_list = ["music", "lego", "netflix", "tech", "tennis", "pets", "coding"]
# While loop version
'''
i = 0
while i < len(my_list):
    print("I like " + my_list[i])
    i += 1
'''
    
# TODO: write your code below
# For loop version
for item in my_list:
    print("I like ", item)

'''
2. Change the first item of my_list (from Q1) to be 'sun'
'''
print("QUESTION 2: ")
# TODO: write your code below
my_list[0] = "sun"
print(my_list)


'''
3. Create a tuple, my_tuple, using the same items in my_list in Q1.
Then, change the first item to be 'ocean'. 
Does it work? Why?
'''
print("QUESTION 3: ")
# TODO: write your code below
my_tuple = ("music", "lego", "netflix", "tech", "tennis", "pets", "coding")
#my_tuple[0] = "ocean" # this line is wrong since tuple is inmmutable 
print(my_tuple)


'''
4. Create a shopping list: apple (count: 1), banana (count: 2), cherry (count: 3), dragonfruit (count 4)
    a. Construct a list of tuples, shopping_list, with each tuple containing a fruit above and its amount, say ("apple", 1).
    b. Print the fruit name whose amount is 2. (You should see "banana")
Hint: 
    Use a for loop to iterate shopping_list and only print the first item of a tuple, whose second item is 2.
'''
print("QUESTION 4: ")

# TODO: write your code below
shopping_list = [("apple", 1), ("banana", 2), ("cherry", 3), ("dragonfruit", 4)]

# Solution 1: for loop iterate the list directly
for tuple in shopping_list:
    if tuple[1] == 2:
        print(tuple[0])

# Solution 2: Use index and range()
for i in range(len(shopping_list)): # range(5) -> 0, 1, 2, 3
    if shopping_list[i][1] == 2: # 
        print(tuple[i][0]) # the first item in the tuple of index i
