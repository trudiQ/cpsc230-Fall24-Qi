# Class Activities (Lecture 17)

'''
Exercise 1: Inventory Management. Use a dictionary to manage a store's inventory.
NOTE: ONLY Use [] operator (NOT methods)
TODO:
a) Create a dictionary named inventory with fruite names as keys and their quantities as values. 
     "apples": 30, "bananas": 45, "oranges": 20.
b) Print the current number of bananas in the inventory.
c) The store received a new batch of 25 bananas. Update the quantity in the inventory and print it.
d) A customer bought 5 oranges. Update the quantity in the inventory and print it.
e) Add a new item to the inventory called "pears" with a quantity of 10 and print the inventory.
f) An item has been discontinued - remove 'apples' from the inventory using the square bracket operator.
    Print the updated inventory dictionary.
'''
print("QUESTION 1")
# write your code below
# a)
inventory = {"apples":30, "bananas":45, "oranges":20}
# b)
banana_amount = inventory["bananas"]
print("bananas:", banana_amount)
# c)
inventory["bananas"] += 25
print(inventory["bananas"])
# d)
inventory["oranges"] -= 5
print(inventory["oranges"])
# e)
inventory["pears"] = 10
print(inventory)
# f)
del inventory["apples"]
print(inventory)


'''
Exercise 2: Inventory Management. Use a dictionary to manage a store's inventory.
NOTE: ONLY Use dictionary methods.
TODO:
a) Create a dictionary named inventory with sample items as keys and their quantities as values. 
     "apples": 30, "bananas": 45, "oranges": 20.
b) Print the current number of bananas in the inventory. Use get()
c) The store received a new batch of 25 bananas. Update the quantity in the inventory and print it. Use update()
d) A customer bought 5 oranges. Update the quantity in the inventory and print it. Use update()
e) Add a new item to the inventory called "pears" with a quantity of 10 and print the inventory. Use update()
f) An item has been discontinued - remove 'apples' from the inventory and print the quantity of apple to be removed.
    Print the updated inventory dictionary. Use pop()
'''
print("QUESTION 2")
# write your code below
# a)
inventory = {"apples":30, "bananas":45, "oranges":20}
#b)
banana_amount = inventory.get("bananas")
print("bananas:", banana_amount)
#c)
inventory.update({"bananas" : banana_amount + 25})
print(inventory.get("bananas"))
#d)
orange_amount = inventory.get("oranges")
inventory.update({"oranges" : orange_amount - 5})
print(inventory.get("oranges"))
#e)
inventory.update({"pears" : 10})
print(inventory)
#f)
apple_amount = inventory.pop("apples")
print(inventory)
