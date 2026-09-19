"""
Problem: Given an array/list of integers, return the largest value.

Input:  [4, 9, 2, 15, 7]
Output: 15

Concepts: loops, comparison logic
"""


def find_max(nums):
    if not nums:
        raise ValueError("Array is empty")
    max_num = nums[0]
    for n in nums[1:]:
        if n > max_num:
            max_num = n
    return max_num


if __name__ == "__main__":
    # Normal case
    print(find_max([4, 9, 2, 15, 7]))
    # Edge case: single element
    print(find_max([7]))
    # Edge case: all negative numbers
    print(find_max([-5, -1, -10]))
