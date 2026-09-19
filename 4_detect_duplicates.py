"""
Problem: Given a list of integers, return True if any value appears
more than once.

Input:  [1, 4, 7, 2, 4]
Output: True

Concepts: Set/HashSet, loops, efficient lookups
"""


def has_duplicates(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    # Normal case
    print(has_duplicates([1, 4, 7, 2, 4]))
    # Edge cases: empty list, all unique
    print(has_duplicates([]))
    print(has_duplicates([1, 2, 3]))
