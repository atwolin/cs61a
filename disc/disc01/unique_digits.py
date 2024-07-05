def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    assert n > 0, "The input number must be positive"
    count = 0
    i = 0
    while i < 10:
        # print(f"i={i}")
        if has_digit(n, i):
            count += 1
            # print(f"n={n}, i={i}, count: {count}")
        i += 1

    return count


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    # print(f"has_digit: {n}, {k}")
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    num_but_last, last = n // 10, n % 10
    while not (num_but_last == 0 and last == 0):
        # print(f"num_but_last={num_but_last}, last={last}")
        if last == k:
            return True
        num_but_last, last = num_but_last // 10, num_but_last % 10
        # print(f"after: num_but_last={num_but_last}, last={last}")
    return False


if __name__ == "__main__":
    from doctest import run_docstring_examples

    run_docstring_examples(unique_digits, globals(), True)
    # num = unique_digits(8675309)
