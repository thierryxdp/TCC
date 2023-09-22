import math

def num_bombons(q,p):
    """Define a quantidade de bombons que consegue-se comprar, sendo q a quantiadade de inheiro e p o preço do bombom"""
    return math.floor(q/p)