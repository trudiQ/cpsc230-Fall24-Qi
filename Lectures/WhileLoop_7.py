# Class Activities (Lecture 7)

'''
0. What's wrong with this while loop and how can you fix it?
'''

#x = 1
#while x < 10:
#     print(x)

# solution
# this results in an infinte loop where x remains 1 the print 1 forever
print("Question 0: ")
x = 1
while x < 10:
     print(x)
     x += 1 # increment x's value to change the evaluation of the condition and end the loop

'''
1. Use a while loop, print out all the numbers between 1 and 10 (including)
'''
print("Question 1: ")
x = 1
while x <= 10:
    print(x)
    x += 1


'''
2. Use a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by BOTH 5 and 9.
Add comment for each line to explain the code
Hint: When a is divisible by b, the remainder of a/b is 0.
    Recall: How to check an even number? (it is a number that is divisible by 2).
'''
print("Question 2: ")
x = 1
while x <= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x, "can be divided by both 5 and 9")
    x += 1

# solution 2:
x = 0
while x < 100:
     x += 1
     if x % 5 == 0 and x % 9 == 0:
          print(x)
    

'''
3. Use a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by both 5 and 9.
Exit the loop when the number is greater than 50.
Use break for this question.
Add comment for each line to explain the code
'''
print("Question 3: ")
x = 1
while x <= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x, "can be divided by both 5 and 9")
    if x > 50: # break when the number is greater than 50
        break
    x += 1


'''
4. Use a while loop, print out all the numbers between 1 and 10 (including) 
except for those which are divisiable by 3.
Use continue for this question.
Add comment for each line to explain the code
'''
print("Question 4: ")
# Solution 1:
x = 1
while x <= 10:
    if x % 3 == 0:
        x += 1 # increament x before continue to update x and avoid infinite loop
        continue
    print(x)
    x += 1

# Solution 2:
x = 0
while x < 10:
    x += 1
    if x % 3 == 0:
        continue
    print(x)