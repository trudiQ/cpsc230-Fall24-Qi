# Homework for Lectures 17 & 18
# Rename the file as HW_10_YOURNAME.py

##----------------------------Dictionary operator and methods ---------------------------
# Question 1: There are five small, related questions (A-C).

'''
A: Create a Car Inventory System, named car_inventory. You work for a vintage car dealership, 
    and you have been tasked with creating an inventory system to track the cars in the showroom. 
    Each car has a unique ID, with details like brand, model, and year.
TODO: Create a dictionary for a car: id: VIN1234567890, brand: Porsche, model: 911, year: 1965
        Print it out.
'''
print("QUESTION 1.A")
# write your code below




'''
B: Update the Inventory. A car enthusiast is interested in a Porsche 911 from 1965 but also wants 
    to know if it comes in red and what its price is. 
    However, this information is missing from your current records.
TODO: Update the car dictionary, car_inventory, from Question 1 to include color and price keys with values 
    "red" and "$100,000" respectively, and print the updated dictionary.
    Can you complete this question using approaches below:
        a) ONLY use [] operator
        b) ONLY use update() method
'''
print("QUESTION 1.B")
# write your code below





'''
C: Good news! Your Porsche 911 has been sold. Now, you need to update the inventory to reflect this sale.
TODO: Remove the "price" key from car_inventory because the car's sale price is confidential.
    Print the dictionary after the removal of the price information to check your answer.
'''
print("QUESTION 1.C")
# write your code below





##----------------------------Iterating a dictionary ---------------------------
'''
Question 2: You are responsible for tracking the growth of trees planted in the school yard. The dictionary below 
    contains the tree species and their height in feet. After a year, it's time to measure them again, and you 
    expect every tree has grown by 10%. 
TODO: Use a for loop to iterate each item in the dictionary,
        calculate the updated height of each tree,
          and print out which trees have reached OVER 15 feet tall after the update.
Hint: Refer to Q4 in the in-class exercise for Lecture 18.
'''
print("QUESTION 2")
trees = {
    "Oak": 12.1,
    "Maple": 15.5,
    "Birch": 9.8,
    "Cherry": 13.9
}
# write your code below


