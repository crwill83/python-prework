# QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
def hello_name(user_name):
    print(f"Hello {user_name.title()}.")

hello_name("johnny")

# QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    odds = 1
    while odds < 100:
        if odds%2 == 1:
            print(
                odds
            )
            odds += 1
        else:
            odds += 1
    
first_odds()

# QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    return(max(a_list))
max_num_in_list([0,1,2,3,4,5])

# QUESTION 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap_year(a_year):
        if (a_year%4 == 0 and a_year%100 != 0) or (a_year%400 == 0):
            return True
        else:
            return False
          
print(is_leap_year(2022))

# QUESTION 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are
# consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def
# is_consecutive(a_list):
def is_consecutive(a_list):
    index = 0
    for index in range(len(a_list) - 1):
        if (a_list[index] + 1) == (a_list[index + 1]) and (index + 1 <= len(a_list)):
            index += 1
        else:
            return False
    return True

print(is_consecutive([1,2,3,4,5]))