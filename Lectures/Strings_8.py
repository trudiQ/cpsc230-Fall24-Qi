# Class Activities (Lecture 8)

'''
1. Create a string 'Hello World!' and store it to a variable named str1.
    a. Print out charater 'H' in this string using index.
    b. Slice this string to get 'ello' and assign it to another variable named str2 and print it.
'''
print("Question 1: ")
str1 = 'Hello World!'
print(str1[0]) # access 'H' using its index
str2 = str1[1:5] # slice a new string using an index range
print(str2)



'''
2. Use the membership operator in to check if 'Hello World!' contains a space, i.e., ' '
    if yes, print out "Yes, there is a space."; otherwise "No space."
'''
print("Question 2: ")
str1 = 'Hello World!'

# Solution 1:
check = ' ' in str1
if check == True:
    print("Yes, there is a space")
else: # meaning check == False
    print("No space")

# Solution 2:
if ' ' in str1:
    print("Yes, there is a space")
else:
    print("No space")



'''
3. Ask the user to input two words and store them into two variables, x and y.
Use addition (+) to add these two variables together and assign the result back to x.
print out x in this format: "Here is the combined word: [result]" where result is the value of x.
'''
print("Question 3: ")
x = input("input a word: ")
y = input("input another word: ")
x += y # equivalent to x = x + y
print("Here is the combined word:", x)



'''
4. Write a while loop to ask the user to input one character (a letter, a number, or a symbol) at a time.
Print whatever they just typed. If they typed nothing and hit enter (they created an empty string), 
print "Nothing was typed. Exit now. " and end the loop using break.
'''
print("Question 4: ")
while True:
    x = input("Please type a character: ")
    if x == "": # this is an EMPTY string
        print("Nothing was typed. Exit now.")
        break
    print(x)






