'''
    Função que calcula a quantidade de carros necessaria para
    uma viagem dado o numero de pessoas viajando (p) e a
    capacidade unica de passageiros dos carros (c),
    prioritariamente 5.
    int, int -> int
'''
from math import ceil
def carros (p, c=5):
    return ceil (p/c)