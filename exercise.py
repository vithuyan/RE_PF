#Exercise 1
# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.
#
# Test it to make sure it works.
def sum_of_odd(list):
    sum = 0
    for num in list:
        if num % 2 != 0:
            sum += num
    return sum

number_list = [1,2,3,4,5,6,7,8,9]            
