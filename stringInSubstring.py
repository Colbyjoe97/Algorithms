# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.

def numOfStrings(patterns, word):
    count = 0
    for i in range(len(patterns)):
        if patterns[i] in word:
            count += 1
    return count

print(numOfStrings(["af", "a", "er", "h"], "after"))