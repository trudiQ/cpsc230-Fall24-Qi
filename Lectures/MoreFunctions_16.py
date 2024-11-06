# Class Activities (Lecture 16)

'''
1. Simulate a simple banking system with functions to deposit, withdraw, and check balance.
    a) Create a global variable account_balance initialized to 0.
    b) Write a function, deposit, with one input parameter, amount, that adds the input amount to account_balance; no return.
    c) Write a function, withdraw, with no input parameter and only subtracts $10 from account_balance each time; no return.
    e) Write a function, check_balance, with no input parameter and only prints the current account_balance; no return.
    f) Perform a series of deposits and withdrawals, and check the balance as below. Print out the result.
        Deposite $100 => Withdraw $10 => Withdraw $10 => Deposite $30 => Check_balance
NOTE: Define all the required functions first and then call them one after another based on f).
'''
print("QUESTION 1: ")
# write your code below
account_balance = 0 # create a global variable

# define all the functions here first
def deposite(amount):
    global account_balance # declare the global variable before changing it
    account_balance += amount
    print("deposite", amount, "dollars") # optional

def withdraw():
    global account_balance
    account_balance -= 10
    print("withdraw 10 dollars") # optional

def check_balance():
    print("Account balance: ", account_balance) # no need 'global account_balance' if not change it


# Perform a series of deposite, withdraw, and check balance
#   Deposite $100 => Withdraw $10 => Withdraw $10 => Deposite $30 => Check_balance
deposite(amount=100)
withdraw()
withdraw()
deposite(amount=30)
check_balance()


'''
2. Write a function, top_3_movies(), that asks the user to input their top 3 favorite movies at once,
separated by ','. Split the string into a list of the 3 movie titles (sub-strings).
Continue asking the user if they DO NOT provide exactly three movies titles.
Return those three movies titles.

Call the function top_3_movies(), and store those 3 movie titles using 3 variables, 
mov1, mov2, and mov3. Print out those 3 movie titles. 
'''
print("QUESTION 2: ")
# write your code below
def top_3_movies():
    movie_titles = [] # create an empty list
    while True:
        user_input = input("Please list three top movies, separated titles by commas: ")
        movie_titles = user_input.split(",")
        if len(movie_titles) == 3:
            break
    return movie_titles[0], movie_titles[1], movie_titles[2]

mov1, mov2, mov3 = top_3_movies()
print("I also like:", mov1, mov2, mov3)



'''
3. You are developing a hotel rating system where customers can give ratings out of 10.
The system calculates the average rating, total number of ratings, and a recommendation status.
    a) Write a function add_hotel_rating(ratings, new_rating) where ratings is a list of existing ratings 
        and new_rating is the new rating given by a new costomer. The function should:
        - add the new rating to the list, rating,
        - calculate the following: 
            total number of ratings, 
            the averaged ratings, and
            a recommendation status: "Recommended" if the average rating is above 7, otherwise "Not Recommended".
        - return the above three values
    b) Call the function with a sample list of ratings [7, 8.1] and a new rating, 6
        and store the returned values in 3 separate variables: average_rating, total_rating_number, recommendation.
        Print out the updated hotel rating details with these THREE variables.
'''
# write your code below
