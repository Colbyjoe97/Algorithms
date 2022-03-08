# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    string = ""
    for word in s.split():
        string += word[::-1] + " "
    return string.rstrip(" ")

# def reverseWords(s):
#     return " ".join([word[::-1] for word in s.split()])

    
print(reverseWords("Let's take LeetCode contest"))

