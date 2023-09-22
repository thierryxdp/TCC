from math import floor
def num_bombons(dinheiro, preco):
    '''funcao que calcula qual o numero maximo de bombons a um preco que se pode comprar com determinado dinheiro; float, float -> int'''
    return floor(dinheiro/preco)