# Class Activities (Lecture 10)

'''
1. Use a for loop and range() to create integers from 0 to 5 (inclusive) and print them out.
'''
print("QUESTION 1:")
# write your code below
for i in range(0, 6, 1):
    print(i)



'''
2. Use a for loop and range() to create integers from 0 to 5 and print them out.
Use a loop variable to count iteration number and print it out after the for loop.
'''
print("QUESTION 2:")
# write your code below
count = 0 # loop variable to keep track of iteration number
for i in range(0, 6, 1):
    print(i)
    count += 1
print("Total iteration number:", count)



'''
3. Use a for loop to iterate a list of numbers, use variable num_neg 
    to count the number of negative numbers (< 0), and print the result.
'''
print("QUESTION 3:")
numbers = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
num_neg = 0 # a counter to keep track of num of negative numbers
# write your code below
for num in numbers:
    if num < 0:
        num_neg += 1
print("There are", num_neg, "negative numbers.")




'''
4. Ask the user to input two words of the SAME LENGTH. If they give words of the same length,
use a for loop, count how many corresponding letters are the same in the two strings. 
For example in 'spam' and 'span', 3 of the letters (s,p,a) are the same. 
In the words 'bitter' and 'better',5 of the letters are the same. 
Print out a message telling the user how many letters are the same.
Hint: 
 1. Get both words' lengths and compare.
 2. Access the corresponding charaters of the same index in both words and compare them.
'''
print("QUESTION 4: ")
# write your code below
# Solution 1: 
word1 = input("Please type the FIRST word: ")
word2 = input("Please type the SECOND word: ")
length1 = len(word1)
length2 = len(word2)
count_same_letters = 0 # counter for tracking the number of same letters
if length1 == length2:
    for i in range(length1):
        if word1[i] == word2[i]: # access and compare the letters of the same index in both words
            count_same_letters += 1 # update the counter
    print(count_same_letters, "of the letter are the same.")
else:
    print("Please type two words of the SAME LENGTH!")

# Solution 2 (NOT REQUIRED):
word1 = input("First word: ")
word2 = input("Second word: ")
count = 0
count_same = 0
len1 = len(word1)
len2 = len(word2)
if len1 == len2:
    for char in word1:
        if char == word2[count]:
            count_same += 1
        count += 1
print("the number of same characters: ", count_same)

