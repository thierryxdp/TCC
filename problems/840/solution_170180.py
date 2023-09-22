from math import *
def quantidade_bolos(a, b, c):
    '''quantidade de bolos possíveis de serem feitos a partir da quantidade de farinha (a), ovos (b) e colheres de sopa de leite (c)'''
    return min(floor(a/2),floor(b/3),floor(c/5))