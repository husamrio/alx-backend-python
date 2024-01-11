#!/usr/bin/env python3
'''Computes the length of a list of sequences.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Annotates the below function’s parameters
    '''
    return [(i, len(i)) for i in lst]
