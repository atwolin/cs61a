def is_prime(n):
    """Returns True if the given positive number, n, is prime, and False otherwise.

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    assert n > 0, "the input number must be positive"
    if n == 1:
        return False

    # Start checking
    i = 1
    while i < n:
        if i != 1 and n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    result = is_prime(9)
    print(result)
