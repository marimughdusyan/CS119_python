# Mari Mughdusyan
# CS 119 Programming in python
# CH12 lab a Largest List Item


# a function that accepts a list as an argument
def max_num(lst):
    # if the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]

    # Recursive case to find the largest item in the list
    else:
        max_of_rest = max_num(lst[1:])
        # return the largest value in the list
        return lst[0] if lst[0] > max_of_rest else max_of_rest


# Create a list with numbers: 10, 20, 30, 40, 50, 60, 70, 80,  90
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#  Pass created list to the recursive function
largest_value = max_num(numbers)

# Display the largest item
print("The largest value is:", largest_value)

# Output
# The largest value is: 90
