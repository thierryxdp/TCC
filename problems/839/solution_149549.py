from math import ceil
def carros(p, c=5):
    ''' função que calcula e retorna o número de carros (c) necessários para transportar um número (p) de pessoas '''
    return ceil(p/c)