# Class Activities (Lecture 4)

'''
Without using Python, figure out the answer to this statement.

    10 + 2 ** 3 - (4+5) + 49/7 * 2

1. What's the Answer? BONUS: will this be a float or int?
2. What Order should we go in?
3. Rewrite this expression using more parenthese to make it
    clearer on what order things are run in.
4. Check your answers using Python.
'''
# your answers here
# 1. 23.0, float, because division results in a float and mix of float and integeters result in a float
# 2. (4+5) -> 2**3 -> 49/7 -> 7 * 2 -> 10 + 8 -> 18 - 9 -> 9 + 14 -> 23.0
# 3. ((10 + (2 ** 3)) - (4+5)) + ((49/7) * 2)
# 4. See below:
result = 10 + 2 ** 3 - (4+5) + 49/7 * 2
print(result)



'''
Using Comparison operators and arithmetic operators, make a complicated 
expression (use at least 5 operators, repeats allowed) that evaluates to False.
Check your answer by printing out the result of the expression (should be a False).
'''
# your answer here
result = 2 * 10 + 3 + 4 == 10 / 2
print(result)