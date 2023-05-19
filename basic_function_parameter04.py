# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average(lst):
    s=0
    for j in lst:
        s+=j
    return s/len(lst)
print(calculate_average([1,2,3,4,5,8]))
