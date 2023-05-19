# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(x):
    print(x)
    i = 0
    n = x[0]
    while i<len(x):
        if x[i]<n:
            n = x[i]
        i = i + 1
    return n

print(find_smallest([10,20,3,94]))