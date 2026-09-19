"""
Problem: Write a function that takes a string and returns the reversed
version of the string.

Input:  "hello"
Output: "olleh"

Concepts: strings, loops, string manipulation
"""


def reverse_string(s):
    return s[::-1]


def reverse_string_manual(s):
    """Manual loop version, in case the interviewer wants the algorithm
    shown rather than relying on slicing syntax."""
    result = ""
    for char in s:
        result = char + result
    return result


if __name__ == "__main__":
    # Normal case
    print(reverse_string("hello"))
    print(reverse_string_manual("hello"))
    # Edge cases: empty string, single character, palindrome
    print(reverse_string(""))
    print(reverse_string("a"))
    print(reverse_string("racecar"))
