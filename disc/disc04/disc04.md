## Tree Recursion

### Q1: Insect Combinatorics

- If the insect hits the upper edge, it should turn right (`n - 1`) and just has only one way to reach the goal.
- If the insect hits the rightmost edge, it should turn up (`m - 1`) and just has only one way to reach the goal.
- If none of the above cases occurs, the insect can turn right or up.

```python
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 0 and n == 0:
        return 1
    if (m == 0 and n != 0) or (m != 0 and n == 0):
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
```

## Lists
### Q2: Even Weighted

1. with a `for` loop
```python
def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    new_x = []
    for i in range(len(x)):
        if i % 2 == 0:
            new_x += [i * x[i]]
    return new_x
```

2. with a list comprehension
```python
def even_weighted_comprehension(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_comprehension(x)
    [0, 6, 20]
    """
    return [i * x[i] for i in range(len(x)) if i % n == 0]
```

## Trees
### Q3: Has Path

- What recursive calls will you make?
  If the current label equals to the first element of the path, then go to the next label (sub-tree) and the next element of the path.
- What type of values do they return?
  `bool`
- What do the possible return values mean?
  There exists at least one path with given labels.
- How can you use those return values to complete your implementation?
  Check if the current label is equals to first element of the path. If `True`, then go to the next label; otherwise, return `False`.

```python
def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == label(t) and is_leaf(t):  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        "*** YOUR CODE HERE ***"
        return(branches(t), p[1:])
```
- Discussion
  Yes, since we have check the first element is valid, then we can use `branches(tree)` to continue to check the rest of sub-tree and path.

### Q4: Find Path

- Recursive call
The recursive case is to check for the rest of labels can reach the node labeled `x`.

```python
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return t
    else:
        path = branches(t)
        if path:
            return [label(t)] + [find_path(p, x) for p in path]
    return None
```
- Discussion
  This function does not have a base case that uses `is_leaf` since the recursive case will check whether the `t` is empty or not. If the `t` is empty, it means there is no path to reach the node labeled `x` and return `None`.


### Q5: Sprout Leaves
```python
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the labels in leaves at each leaf of
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), leaves)

    return tree(label(t) + list(sprout_leaves(path) for path in branches(t)))
```
> The recursive case is to keep the current root of `t` and then dive into all of branches of the `t`.

## Extra Practice
### Q6: Tree Deciphering

- `max([t1, t2], key=label)` returns the tree with the largest label. Let `A` be `max([t1, t2], key=label)`.
- `branches(A)` returns the branches of the tree with the largest root label between `t1` and `t2`. Let `B` be `branches(A)`.
- `min(B, key=label)` returns the tree with the smallest label among the branches of the tree. Let `C` be `min(B, key=label)`.
- `label(C)` returns the root label of the tree with smallest label among the subtrees.

Therefore, `result` is the root label of the sub-tree, whose parent tree has larger root label than another tree compared with, with the smallest root label of all sub-trees.
