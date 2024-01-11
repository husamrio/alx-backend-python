#!/usr/bin/env python3
'''Computes the length of a list of sequences.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Duck typing - first element of a sequence
    returns first element of list or None
    '''
    return [(i, len(i)) for i in lst]
