import math
def num_bombons (d,p):
    """cálculo do numero de bombons que é possivel comprar dado o dinheiro d e o preço p:
    float,float -> int"""
    return math.floor(d/p)