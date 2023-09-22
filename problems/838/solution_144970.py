import math
def num_bombons(x,y):
    """funçao que calcula quantos bombons posso comprar dados o dinheiro(x) e o preço(y)"""
    return math.floor(x//y)