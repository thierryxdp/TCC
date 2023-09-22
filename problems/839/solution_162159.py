from math import ceil
def carros(p,c):
    '''Retorna o número de carros com "c" lugares necessários para o transporte de "p" passageiros.'''
    return ceil(p/c)

def carros(p):
    '''Retorna o número de carros com cinco lugares necessários para o transporte de "p" passageiros.'''
    return ceil(p/5)