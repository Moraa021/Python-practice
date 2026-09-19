"""
Problem: Given a list of words, count how many times each word appears.

Input:  ["apple", "banana", "apple", "orange", "banana", "apple"]
Output: {"apple": 3, "banana": 2, "orange": 1}

Concepts: HashMap/dict, loops, counting logic
"""


def word_count(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    # Normal case
    print(word_count(["apple", "banana", "apple", "orange", "banana", "apple"]))
    # Edge case: empty list
    print(word_count([]))
