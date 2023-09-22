import math
def num_bombons (d, p):
    '''Calcula o quantos bombons podem ser comprados, dados d = dinheiro
    e p = preço do bombom'''
    return round(d//p)