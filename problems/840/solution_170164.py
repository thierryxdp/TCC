import math

def xicara (A):
    '''quantidade de xícaras para fazer cada bolo'''
    return math.floor (A/2)
def ovos (B):
    '''quantidade de ovos para fazer cada bolo'''
    return math.floor (B/3)
def colheres (C):
    '''quantidade de colheres para fazer cada bolo'''
    return math.floor (C/5)
def bolos (A,B,C):
    '''retorna quantidade de bolos joão consegue fazer com uma quantidade A, xícaras de farinha de trigo,
    B, ovos, C, colheres de sopa de leite.'''
    return min(xicara (A),ovos (B),colheres (C))