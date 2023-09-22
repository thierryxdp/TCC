from math import *
def carros(pessoas,carros=5):
    '''Função calcula a quantidade de carros, com capacidade (carros),
    para transportar uma quantidade (pessoas) de pessoas'''
    return ceil(pessoas/carros)