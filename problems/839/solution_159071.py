import math 
def carros (p, v=5):
    """retorna a quantidade de carros necessária para uma quantidade de pessoas"""
    return math.ceil (p/v)