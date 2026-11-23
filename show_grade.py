"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "029e5d9ead1632280c8565f3ae5f0218"
GRADE_HASH = "3610bb4a81afc3718253c76b77188dd62a59a44c728c5b578637f89e0699b43d"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
