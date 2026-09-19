"""
Problem: Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is
valid (every opening bracket is closed by the same type, in the
correct order).

Input:  "{[()]}"
Output: True

Input:  "{[(])}"
Output: False

Concepts: stack (list used as a stack), dict for bracket pairs
"""


def is_valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        # any other character is ignored in this simple version
    return len(stack) == 0


if __name__ == "__main__":
    # Normal case
    print(is_valid_parentheses("{[()]}"))
    # Edge cases: mismatched order, empty string, unclosed bracket
    print(is_valid_parentheses("{[(])}"))
    print(is_valid_parentheses(""))
    print(is_valid_parentheses("((("))
