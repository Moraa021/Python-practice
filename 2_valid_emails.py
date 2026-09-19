"""
Problem: Given a list of email addresses, return only the valid ones
based on a simple validation rule.

Input:  ["amy@test.com", "invalid-email", "john@example.com", "hello"]
Output: ["amy@test.com", "john@example.com"]

Concepts: strings, conditionals, validation
"""


def valid_emails(emails):
    valid = []
    for email in emails:
        if email.count("@") == 1:
            local, domain = email.split("@")
            if local and "." in domain and not domain.startswith("."):
                valid.append(email)
    return valid


if __name__ == "__main__":
    # Normal case
    print(valid_emails(["amy@test.com", "invalid-email", "john@example.com", "hello"]))
    # Edge cases: empty string, multiple @, no domain dot
    print(valid_emails(["", "a@b@c.com", "noatsign.com", "a@b"]))
