import math
def carros (p,q=5):
    '''Função que dá a quantidade de veiculos dados o número de pessoas que irão viajar'''
    return math.ceil(p/q)