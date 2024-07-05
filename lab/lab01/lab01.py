def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    i = 1
    result = n
    while i < k:
        result *= n - i
        i += 1
    return result


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    if n < k:
        return 0
    num_divisible = 0
    i = 1
    while i <= n:
        if i % k == 0:
            print(i)
            num_divisible += 1
        i += 1
    return num_divisible


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    num_but_last, last = y // 10, y % 10
    digits = 0
    while not (num_but_last == 0 and last == 0):
        digits += last
        num_but_last, last = num_but_last // 10, num_but_last % 10
    return digits


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return False
    num_but_last, last = n // 10, n % 10
    while not (num_but_last == 0 and last == 0):
        is_eight = last == 8
        num_but_last, last = num_but_last // 10, num_but_last % 10
        if is_eight and (last == 8):
            return True
    return False
