from math import ceil

def carros (p,c=5):
    '''funcao que retorna o numero de veiculos necessarios para transportar
    um numero p de pessoas, levando em consideracao sua capacidade de transporte c
    int,int,int -> int'''
    return ceil(p/c)