from math import ceil
def carros(p;c=5):
    '''Retorna a quantidade de carros com cinco lugares necessários para transportar uma quantidade "p" de passageiros.'''
    return ceil(p,c)