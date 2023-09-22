from math import floor
def num_bombons(x,y):
    '''funcao que calcula qual o numero maximo de bombons a um preco (x) que se pode comprar com determinado dinheiro (y); float, float -> int'''
    return floor(y/x)