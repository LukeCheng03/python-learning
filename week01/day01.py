def is_even(num):
    """Return True if the number is even, otherwise False."""
    if num % 2 == 0:
        return True
    return False

def average(nums):
    """Return the average of a list of numbers"""
    return sum(nums)/len(nums)

def count_vowels(text):
    """Return the number of vowels(a, e, i, o, u) in a string"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count