from math import *
def carros(p,c=5):
    '''Função que recebe a quantidade de pessoas (p)
    calcula e retorna o numero exato de carros com capacidade (c)
    para realizar a viagem'''
    return ceil(p/c)