import math
from math import *

def hashtag(s):
    """Dada uma string insere um # no início, meio e fim.
    str -> str"""
    
    metade = math.floor(s.length / 2);
    resultado = '#' + s.substr(0,metade) + '#' + s.substr(metade) + '#';
    
    return resultado