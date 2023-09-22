from math import*
def num_bombons (dinheiro, preco):
    '''Calcula a quantidade de bombos que se pode comprar
    dado o dinheiro e o preço unitário
    float, float -> int'''
    return math.floor(dinheiro,preco)