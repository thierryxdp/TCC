from math import *
def carros(p, c=5):
    '''retorna o numero de carros(c) necessarios
    para transportar uma certa quantidade de 
    pessoas(p)'''
    return ceil(p/c)