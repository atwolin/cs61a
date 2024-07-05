def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return True
    num_but_last, last = x // 10, x % 10
    while not (num_but_last == 0 and last == 0):
        num_but_last_two, last_two = num_but_last // 10, num_but_last % 10
        # print(
        #     f"num_but_last={num_but_last}, last={last}, num_but_last_two={num_but_last_two}, last_two={last_two}"
        # )
        if last_two > last:
            return False
        num_but_last, last = num_but_last_two, last_two
    return True


if __name__ == "__main__":
    result = ordered_digits(11)
