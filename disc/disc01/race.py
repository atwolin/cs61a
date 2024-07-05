def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, "the hare must be fast but not too fast"
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
        print(f"{minutes}: tortoise: {tortoise}, hare: {hare}")
    return minutes


if __name__ == "__main__":
    # Returns the wrong value
    x_input, y_input = 3, 5

    # Runs forever
    # x_input, y_input = 3, 4

    min = race(x_input, y_input)
    print(f"min: {min}")
