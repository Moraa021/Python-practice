"""
Problem: Review a code snippet and explain what's wrong, why it happens,
and how to fix it.

Below: a broken version of find_max, followed by the corrected version,
so I can compare and explain the bug during the interview.
"""


# --- BROKEN VERSION ---
def find_max_broken(nums):
    max_num = 0  # BUG 1: assumes 0 is always a safe starting point
    for i in range(len(nums) + 1):  # BUG 2: off-by-one, goes out of range
        if nums[i] > max_num:
            max_num = nums[i]
    return max_num


# What's wrong:
# 1. `max_num = 0` fails if every number in the list is negative -
#    it would incorrectly return 0 instead of the true (negative) max.
# 2. `range(len(nums) + 1)` causes an IndexError, since valid indices
#    only go from 0 to len(nums) - 1.

# Why it happens:
# - Starting max at a fixed value ignores lists where the real max is
#   smaller than that value.
# - The range is one step too long, so the loop tries to access an
#   index that doesn't exist.


# --- FIXED VERSION ---
def find_max_fixed(nums):
    if not nums:
        raise ValueError("Array is empty")
    max_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
    return max_num


if __name__ == "__main__":
    # This call will raise IndexError - demonstrates BUG 2
    # print(find_max_broken([4, 9, 2, 15, 7]))

    # Fixed version - normal case
    print(find_max_fixed([4, 9, 2, 15, 7]))
    # Fixed version - edge case: all negative (would have failed BUG 1)
    print(find_max_fixed([-5, -1, -10]))
    # Fixed version - edge case: single element
    print(find_max_fixed([7]))
