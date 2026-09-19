"""
Problem: Given a list of log messages, count how many contain the
word "ERROR".

Input:  ["INFO: started", "ERROR: failed to connect", "ERROR: timeout", "INFO: done"]
Output: 2

Concepts: loops, string matching, debugging mindset
"""


def count_errors(logs):
    return sum(1 for log in logs if "ERROR" in log)


def count_errors_case_insensitive(logs):
    """Use this version if the interviewer clarifies that matching
    should not be case-sensitive (e.g. 'error' should also count)."""
    return sum(1 for log in logs if "error" in log.lower())


if __name__ == "__main__":
    logs = ["INFO: started", "ERROR: failed to connect", "ERROR: timeout", "INFO: done"]
    # Normal case
    print(count_errors(logs))
    # Edge case: empty list
    print(count_errors([]))
    # Edge case: mixed casing
    print(count_errors_case_insensitive(["error: minor", "ERROR: major", "Warning: none"]))
