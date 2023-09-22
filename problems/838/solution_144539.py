import math
def num_bombons(dinheiro,preco):
    '''Função que calcula o número de bombons de determinado valor 
    (preco) que se pode comprar com determinada quantia (dinheiro)
    float, float -> int'''
    return math.round(dinheiro/preco)