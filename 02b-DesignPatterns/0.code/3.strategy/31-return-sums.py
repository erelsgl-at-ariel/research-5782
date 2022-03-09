"""
Number partitioning algorithms - naive implementation - returns only the sums.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import List

def roundrobin(numbins: int, items: List[float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> roundrobin(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 3, 1], [9, 3], [5, 2]]
    """
    bins = [[] for _ in range(numbins)]
    ibin = 0
    for item in sorted(items, reverse=True):
        bins[ibin].append(item)
        ibin = (ibin+1) % numbins
    return bins


def roundrobin_sums(numbins: int, items: List[float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin_sums(numbins=2, items=[1,2,3,3,5,9,9])
    [18, 14]
    >>> roundrobin_sums(numbins=3, items=[1,2,3,3,5,9,9])
    [13, 12, 7]
    """
    sums = [0 for _ in range(numbins)]
    ibin = 0
    for item in sorted(items, reverse=True):
        sums[ibin] += item
        ibin = (ibin+1) % numbins
    return sums


def greedy(numbins: int, items: List[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the partition.

    >>> greedy(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]
    """
    bins = [[] for _ in range(numbins)]
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sum(bins[i]))
        bins[index_of_least_full_bin].append(item)
    return bins


def greedy_sums(numbins: int, items: List[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the sums.

    >>> greedy_sums(numbins=2, items=[1,2,3,3,5,9,9])
    [16, 16]
    >>> greedy_sums(numbins=3, items=[1,2,3,3,5,9,9])
    [11, 10, 11]
    """
    sums = [0 for _ in range(numbins)]
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sums[i])
        sums[index_of_least_full_bin] += item
    return sums



if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
