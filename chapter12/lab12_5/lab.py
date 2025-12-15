# Mari Mughdusyan
# CS 119 Programming in python
# CH12 lab 5 Recursive List Sum

# A function that accepts a list of numbers as an argument
def list_sum(lst):
    # if the list doesn't have elements return 0
    if len(lst) == 0:
        return 0

    # recursively calculate the sum of all the numbers in the list and return that value
    else:
        return lst[0] + list_sum(lst[1:])


# Create a list with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#  Pass created list to the recursive function
sum_of_list = list_sum(numbers)

# Display the sum
print(f"The sum of the items in the list is: {sum_of_list}")
