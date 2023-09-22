import math
def num_bombons(dinheiro, preco):
    """retorna a quantidade de bombons que se pode comprar, tendo como entrada o dinheiro atual e o preço de cada bombom; float, float -> int"""
    return math.floor(dinheiro/preco)