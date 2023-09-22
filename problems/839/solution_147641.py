def carros(p,c=5):
    """calcula o número de carros de c capacidade necessários para uma viagem com p pessoas"""
    from math import *
    x = p/c
    return ceil(x)