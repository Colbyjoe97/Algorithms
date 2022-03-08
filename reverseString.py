# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# NO BUILT IN METHODS
# def reverseString(s):
#     for i in range(len(s) / 2):
#         temp = s[i]
#         s[i] = s[len(s)-1-i]
#         s[len(s)-1-i] = temp
#     return s

# USING BUILT IN METHODS
# def reverseString(s):
#     return s.reverse()

# Slicing
def reverseString(s):
    return s[::-1]



print(reverseString("Hello"))