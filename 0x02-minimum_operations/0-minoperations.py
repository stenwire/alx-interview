#!/usr/bin/python3
"""Solution for minimum operations"""


def minOperations(n: int) -> int:
    """Minimum number of operations needed to get n H characters"""

    if n <= 1:
        return 0

    len_text = 2  # at this point a copy and paste op has been done
    prev = 1    # one character was added to the end
    op = 2

    while True:
        # check if the number of char is present is divisible by n
        if n % len_text == 0 and len_text != n:
            prev = len_text
            len_text = len_text * 2  # performs a copy and paste op
            op += 2
        elif len_text == n:
            break
        else:
            len_text += prev  # perform a paste operation only
            op += 1
    return op
