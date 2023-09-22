from math import ceil

def carros (p,c):
    '''Dado um número de pessoas e o capacidade do veículo
    calcule a quantidade de veículos necessários'''
    return ceil (p/c)