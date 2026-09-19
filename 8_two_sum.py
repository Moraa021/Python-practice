"""
Problem: Given a list of integers and a target sum, return the indices
of the two numbers that add up to the target.

Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   (because nums[0] + nums[1] == 9)

Concepts: dict/HashMap for O(n) lookups, loops
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no pair found


if __name__ == "__main__":
    # Normal case
    print(two_sum([2, 7, 11, 15], 9))
    # Edge case: no valid pair
    print(two_sum([1, 2, 3], 100))
    # Edge case: empty list
    print(two_sum([], 5))
