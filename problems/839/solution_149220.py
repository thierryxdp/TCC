from math import *
def carros (p,c=5):
    '''Calcula o numero de carros necessarios para p pessoas poderem viajar
    em carros com capacidade total de passageiros c'''
    return ceil(p//c)