"""
    Number partitioning algorithms - naive implementation - both lists and dicts
"""

from typing import Dict

def roundrobin(numbins: int, items: Dict[str, float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> roundrobin(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 3, 1], [9, 3], [5, 2]]

    >>> roundrobin(numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'd', 'a'], ['g', 'c', 'b']]
    >>> roundrobin(numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'c', 'a'], ['g', 'd'], ['e', 'b']]
    """
    if isinstance(items, dict):  # items is a dict mapping an item to its value.
        item_names = items.keys()
        map_item_to_value = lambda item: items[item]
    else:  # items is a list
        item_names = items
        map_item_to_value = lambda item: item

    bins = [[] for _ in range(numbins)]
    ibin = 0
    for item in sorted(item_names, key=map_item_to_value, reverse=True):
        bins[ibin].append(item)
        ibin = (ibin+1) % numbins
    return bins



def greedy(numbins: int, items: Dict[str, float]):
    """
    Partition the given items using the greedy number partitioning algorithm.

    >>> greedy(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]

    >>> greedy(numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'b'], ['g', 'c', 'd', 'a']]
    >>> greedy(numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'b'], ['g', 'a'], ['e', 'c', 'd']]
    """
    if isinstance(items, dict):  # items is a dict mapping an item to its value.
        item_names = items.keys()
        map_item_to_value = lambda item: items[item]
    else:  # items is a list
        item_names = items
        map_item_to_value = lambda item: item

    bins = [[] for _ in range(numbins)]
    sums = [0 for _ in range(numbins)]
    for item in sorted(item_names, key=map_item_to_value, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sums[i])
        bins[index_of_least_full_bin].append(item)
        sums[index_of_least_full_bin] += map_item_to_value(item)
    return bins


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
