from math import ceil
def carros(pessoas,capacidade=5):
    '''Função que calcula e retorna o número de carros, dos valores de entrada de pessoas e capacidade
       int, int→int'''
    return ceil(pessoas/capacidade)