"""Hacker Rank Challenges"""
import re

S = "aaabbabaakldaaaaa"
k = "aa"

# Find all matches using finditer with positive lookahead
matches = list(re.finditer(f'(?={k})', S))

# If no matches found
if not matches:
    print((-1, -1))
else:
    # Print all matches with corrected end index
    print(f"There are {len(matches)} case(s) that {k} occurred")
    print()
    for match in matches:

        start = match.start()
        # End index should be start + len(k) - 1 to match the sample outpwut
        end = start + len(k) - 1
        print(f"{(start, end)}")