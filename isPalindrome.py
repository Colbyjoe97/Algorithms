# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# SOLUTION

def isPalindrome(x):
    palindrome = True
    num = str(x)
    for i in range(len(num)):
        if num[i] != num[len(num)-1-i]:
            palindrome = False
    return palindrome
print(isPalindrome(12121))