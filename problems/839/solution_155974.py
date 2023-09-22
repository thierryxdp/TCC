from math import ceil
def carros(pessoas,capacidade=5):
    '''Calcula a quantidade de carros de capacidade X para transportar
    um número Y de pessoas.
    int,int -> int'''
 
    return ceil(pessoas / capacidade)