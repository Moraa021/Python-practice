"""
Problem: Merge two lists into one sorted list, removing duplicates.

Input:  list1 = [3, 1, 5], list2 = [5, 2, 1]
Output: [1, 2, 3, 5]

Concepts: sets for de-duplication, sorted() for ordering
"""


def merge_sorted_unique(list1, list2):
    return sorted(set(list1) | set(list2))


if __name__ == "__main__":
    # Normal case
    print(merge_sorted_unique([3, 1, 5], [5, 2, 1]))
    # Edge cases: one empty list, both empty
    print(merge_sorted_unique([], [1, 2]))
    print(merge_sorted_unique([], []))
