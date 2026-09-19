"""
Problem: Given a list of integers, return the most frequently
occurring value. If there's a tie, return any one of the top values.

Input:  [1, 3, 3, 2, 1, 1]
Output: 1

Concepts: dict/HashMap, loops, max with key function
"""


def most_common(nums):
    if not nums:
        return None
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return max(counts, key=counts.get)


if __name__ == "__main__":
    # Normal case
    print(most_common([1, 3, 3, 2, 1, 1]))
    # Edge cases: empty list, single element, all same
    print(most_common([]))
    print(most_common([5]))
    print(most_common([9, 9, 9]))
