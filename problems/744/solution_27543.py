import math
from math import *

def hashtag(s):
    """Dada uma string insere um # no início, meio e fim.
    str -> str"""
    
    f = math.floor(s[0:].length / 2)
    
    return '#' + s.substr[0:f] + '#' + s.substr[f:] + '#'