"""
Problem: Given an array of n distinct integers taken from the range
0 to n (inclusive), find the one number in that range that is
missing from the array.

Input:  [3, 0, 1]
Output: 2   (range is 0..3, and 2 is missing)

Concepts: math (sum formula), arrays
"""


def find_missing(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2  # sum of 0..n
    return expected_sum - sum(arr)


if __name__ == "__main__":
    # Normal case
    print(find_missing([3, 0, 1]))
    # Edge cases: missing number is 0, missing number is n
    print(find_missing([1, 2, 3]))
    print(find_missing([0, 1, 2]))
