"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def is_palindrome(word):
    return word == word[::-1]


word = 'civic'
if (is_palindrome(word)):
    print('Yes')
else:
    print('No')
