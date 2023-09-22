import math
from math import floor
def num_bombons(p,d):
    '''Calculo do numero de bombons que podem ser comprados com dados preco(p) e dinheiro(d)'''
    N=d/p
    return math.floor(N)