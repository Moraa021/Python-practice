"""
Problem: Given a list of strings, group the ones that are anagrams
of each other.

Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
(order of groups/items may vary)

Concepts: dict/HashMap, string sorting as a grouping key
"""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


if __name__ == "__main__":
    # Normal case
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Edge cases: empty list, no anagrams, empty strings
    print(group_anagrams([]))
    print(group_anagrams(["abc", "def"]))
    print(group_anagrams(["", ""]))
