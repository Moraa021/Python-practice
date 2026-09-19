"""
Problem: Given a nested list of integers, flatten it into a single
list of integers.

Input:  [1, [2, 3, [4, 5]], 6, [7]]
Output: [1, 2, 3, 4, 5, 6, 7]

Concepts: recursion, lists, type checking
"""


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # Normal case
    print(flatten([1, [2, 3, [4, 5]], 6, [7]]))
    # Edge cases: empty list, no nesting, deeply nested
    print(flatten([]))
    print(flatten([1, 2, 3]))
    print(flatten([[[[1]]], 2]))
