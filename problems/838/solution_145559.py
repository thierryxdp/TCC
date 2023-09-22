import math
def num_bombons(dinheiro,preço):
    """calcula a maior quantidade de bombom de acordo com o preco e o dinheiro q se tem, e o valor de troco
    float,float - int,float"""
    return int(dinheiro/preço),float(dinheiro%preço)