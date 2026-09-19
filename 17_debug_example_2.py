"""
Problem: Review a code snippet and explain what's wrong, why it
happens, and how to fix it.

Below: a broken function that looks up a user's role from a
dictionary, followed by the corrected version.
"""


# --- BROKEN VERSION ---
def get_user_role_broken(users, user_id):
    return users[user_id]["role"]
    # BUG: if user_id is not in the dict, this raises a KeyError.
    # If it IS in the dict but "role" key is missing/typo'd
    # (e.g. stored as "Role"), this also raises a KeyError.


# What's wrong:
# - Directly indexing a dict with `[]` assumes the key always exists.
#   There's no handling for a missing user_id or a missing "role" field.

# Why it happens:
# - Real data is often incomplete: a user record might be malformed,
#   partially created, or the id might simply not exist yet.


# --- FIXED VERSION ---
def get_user_role_fixed(users, user_id):
    user = users.get(user_id)
    if user is None:
        return None  # or raise a custom, clearer exception
    return user.get("role")  # returns None if "role" key is missing


if __name__ == "__main__":
    users = {
        1: {"name": "Amy", "role": "admin"},
        2: {"name": "John"},  # missing "role" on purpose
    }

    # This line would crash with BUG - demonstrates the missing-key issue
    # print(get_user_role_broken(users, 99))

    # Fixed version - normal case
    print(get_user_role_fixed(users, 1))
    # Fixed version - edge case: user exists but role missing
    print(get_user_role_fixed(users, 2))
    # Fixed version - edge case: user_id doesn't exist at all
    print(get_user_role_fixed(users, 99))
