# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(s):
    count = 0
    i = 0
    while i<len(s):
        if s[i] in 'aeiouAEIOU':
            count +=1
        i +=1
    return count
asdfa =count_vowels('aqwer')  
print(asdfa)   
