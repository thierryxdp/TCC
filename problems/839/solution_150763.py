from math import ceil
def carros (p,c=5):
    '''Retorna quantos carros de capacidade c serão necessários para transportar uma quantidade de pessoas p'''
    return ceil(p/c)