# Python Practice

Common Python interview questions and solutions, used to prepare for
live coding interviews (QA Automation Engineer roles).

Each file is self-contained: it includes the problem statement in a
docstring, a solution, and a `__main__` block that runs a normal case
plus at least one edge case.

## How to run any file

```bash
python3 <filename>.py
```

## Core Practice Questions (from Tufin/Tana prep guide)

| # | File | Topic | Concepts |
|---|------|-------|----------|
| 1 | `1_word_count.py` | Count word frequency in a list | dict, loops, counting |
| 2 | `2_valid_emails.py` | Filter valid email addresses | strings, conditionals, validation |
| 3 | `3_find_max.py` | Find the largest number in an array | loops, comparison |
| 4 | `4_detect_duplicates.py` | Detect duplicate values in a list | set, lookups |
| 5 | `5_debug_example.py` | Debug a broken find-max function | off-by-one, bad initial value |
| 6 | `6_reverse_string.py` | Reverse a string | strings, slicing, loops |
| 7 | `7_count_error_logs.py` | Count log lines containing "ERROR" | strings, loops, matching |

## Extra Practice Questions

| # | File | Topic | Concepts |
|---|------|-------|----------|
| 8 | `8_two_sum.py` | Find two numbers that add up to a target | dict, O(n) lookups |
| 9 | `9_is_palindrome.py` | Check if a string is a palindrome | strings, two pointers |
| 10 | `10_flatten_list.py` | Flatten a nested list | recursion |
| 11 | `11_most_common_element.py` | Find the most frequent value in a list | dict, counting |
| 12 | `12_group_anagrams.py` | Group strings that are anagrams | dict, sorting as a key |
| 13 | `13_fizzbuzz.py` | Classic FizzBuzz | loops, modulo, conditionals |
| 14 | `14_valid_parentheses.py` | Check if brackets are balanced | stack |
| 15 | `15_merge_sorted_lists.py` | Merge two lists, sorted, no duplicates | sets, sorted() |
| 16 | `16_missing_number.py` | Find the missing number in a 0..n range | math/sum formula |
| 17 | `17_debug_example_2.py` | Debug a broken dictionary lookup | KeyError handling, .get() |

## How to Approach Live Coding

1. **Understand** — restate the problem and clarify assumptions
   (inputs, outputs, edge cases) before writing any code.
2. **Explain** — briefly describe your approach and which data
   structure you're choosing, and why.
3. **Code** — start with a simple, working solution first.
4. **Think aloud** — narrate what you're doing as you type.
5. **Check edge cases** — empty input, null/None values, duplicates,
   invalid data.
6. **Test** — run through a normal case and at least one edge case.
7. **Respond to hints** — adjust your approach if the interviewer
   nudges you in a different direction.

If stuck, stop typing and talk through the problem out loud instead
of changing code at random.
