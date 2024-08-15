## Getting Started

### Q1: Warm Up

(lambda x: 3)(5) -> 3
(lambda x: 2 * 3 * x)(5) -> 30
result = 30

## Environment Diagrams

### Q2: Bottles
- 1): d
- 2): c
- 3): c

### Q3: Double Trouble

- Global frame
  - double -> func double(x)
  - triple -> func triple(x)
  - hat -(-> double)- -> func double(x)
  - double -(-> triple)- -> func triple(x)

## Call Expressions

- Global frame
  - team -> func team(work)
  - dream -> func dream(work, s)
  - work -> 3
  - t -> abs
  - team -> func dream(work, s) and t

- f1: dream [parent=Global]
  - work -> func team(work)
  - s -> 4
  - t -> not s == True
  Return Value -> not t == False

- f2: team [parent=f1]
  - work -> s - 2  == 2
  Return Value -> t(work) - 1  == 1

- f3: t [parent=f2]
  Return Value -> abs(work) == 2

## Higher-Order Functions

### Q4: Make Keeper
```python
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    assert n > 0, "the input is needed to be positive."
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
    return f
```
`make_keeper` has one parameter `n`. `n` must be a positive integer. `make_keeper` returns function `f`. `f` has only one parameter `cond`, which is an one-argument function and returns a true or a false, and will go through from 1 to `n` (including `n`). If `cond` returns a true value, `f` will print the current number.

### Q5: Digit Finder
```python
def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"
    return lambda x: (k % (10 ** x) // (10 ** (x - 1)))
```

### Q6: Match Maker
```python
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if __________________________:
                return False
            x //= 10
        return True
    return check
```