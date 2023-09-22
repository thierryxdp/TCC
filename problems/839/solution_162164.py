from math import ceil
def carros(p,c=5):
    '''Retorna o número de carros com "c" lugares necessários para o transporte de "p" passageiros.'''
    return ceil(p/c)