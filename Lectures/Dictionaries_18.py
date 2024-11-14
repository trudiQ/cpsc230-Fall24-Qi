# Class Activities (Lecture 18)

# iterate over keys using keys()
'''
Q1: Given a dictionary of stock prices below, prints out all the stock names in uppercase.

Expected Output:
APPLE
MICROSOFT
AMAZON
NVIDIA

Hint: Use for loop to iterate each key and use a string method to uppercase it (check Lecture 9)
'''
print("QUESTION 1: ")
stocks = {"Apple": 224, "Microsoft": 423, "Amazon": 208, "NVIDIA": 148}
# write your code below
for key in stocks.keys():
    print(key.upper())



# iterate over values using values()
'''
Q2: Given a grocery cart below, write some codee to calculate the total price of all items in it - the sum of
all the values in the dictionary, where the fruit name is the key and the value is the price per item. 
Assume each fruit has a quantity of one.

Expected Output:
"Total cost is: $2.74"

Hint: 
    - Use a for loop to iterate all the values in the dictionary, and add each value to a counter 
to get the sum of all the values.
'''
print("QUESTION 2:")
cart = {"banana": 0.99, "apple": 0.50, "peach": 1.25}
# write your code below
total_cost = 0
for value in cart.values():
    total_cost += value

print("Total cose is: $" + str(total_cost))

# Or, you may use f-string:
# print(f"Total cost is ${total_cost}")




# iterate over items using items()
'''
Q3: Following Q1, iterate each item in stocks and print out the company name whose stock price is over $210

Expected Output:
Apple
Microsoft

Hint: Use a for loop to iterate over items, key and value pairs, in a dictionary.
'''
print("QUESTION 3:")
# write your code below
for key, value in stocks.items():
    if value > 210:
        print(key)


'''
Q4: Follow Q2, due to inflation, each the price of each fruit in your grocery cart, cart, has been increased 
    with banana by 10%, apple by 15%, and peach by 20%. Re-calculate the total cost.

Expected Output:
Updated total cost is: $3.16

Hint: 
    - Use a for loop to iterate over items, key and value pairs, in a dictionary;
    - Use if/elif to check each key and add an updated value to the sum.
    - Given a price of $10, when increase by 10%, the new price is 10 * (1 + 0.1) => 11
    - To print two decimal places, you can use f-strings (formatted string literals):
        number = 3.14159
        print(f"{number:.2f}")
        >>> 3.14
        To print the number in a sentence:
        print(f"The number is {number:.2f}")
        >>> The number is 3.14
'''
print("QUESTION 4:")
# write your code below
updated_total_cost = 0
for key, value in cart.items():
    if key == "banana":
        updated_total_cost += value * (1 + 0.1)
    elif key == "apple":
        updated_total_cost += value * (1 + 0.15)
    elif key == "peach":
        updated_total_cost += value * (1 + 0.2)
print(f"Updated total cose is {updated_total_cost:.2f}")
        


### EXTRA QUESTION TO PRACTICE ###
'''
Q5: Given two lists, one with student names and the other with their respective grades, 
    create a dictionary, named student_record, that maps each student to their grade.
    Print out the dictionary.

Expected Dictionary Output:
{"Emma": "A", "Olivia": "B", "Noah":"C", "Liam":"A"}

Hint: 
    - Create student_record as an empty dictionary first
    - Use a for loop with range(0, len(names)) to iterate items in both lists, names and grades, by the indices
    - First list, names, contains keys, and second list, grades, contain values respectively
    - Add each pair of (key, value) to the dictionary, student_record.
'''
print("QUESTION 5:")
names = ["Emma", "Olivia", "Noah", "Liam"]
grades = ["A", "B", "C", "A"]
# write your code
student_record = {} # create an empty dictionary
for i in range(0, len(names)):
    name = names[i]
    grade = grades[i]
    student_record[name] = grade # or, student_record.update({name, grade})
    print(i, "added", name, grade) # this is not required, just show you what iteration looks like
print(student_record)