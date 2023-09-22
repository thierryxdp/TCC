from math import ceil

def carros(num_pes,capacidade=5):
    '''A funcao retorna o numero minimo de carros com capacidade
igual 5 para carregar um dado numero de pessoas(num_pes)'''
    return ceil(num_pes/capacidade)