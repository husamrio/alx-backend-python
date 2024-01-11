#!/usr/bin/env python3
'''Converts a key and its value to a tuple of the key and
    the square of its value.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Takes a string and int/float and returns a tuple
    '''
    return (k, float(v**2))
