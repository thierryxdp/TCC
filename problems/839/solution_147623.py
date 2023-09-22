import math
def carros(p,c=5):
    """calcula e retorna o número exato de carros necessários para uma viajem de p pessoas em carros com capacidade c"""
    return math.ceil(p/c)