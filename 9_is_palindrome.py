"""
Problem: Given a string, return True if it is a palindrome
(reads the same forwards and backwards), ignoring case and spaces.

Input:  "Was it a car or a cat I saw"
Output: True

Concepts: strings, two-pointer technique, normalization
"""


def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    # Normal case
    print(is_palindrome("Was it a car or a cat I saw"))
    # Edge cases: empty string, single char, not a palindrome
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("hello"))
