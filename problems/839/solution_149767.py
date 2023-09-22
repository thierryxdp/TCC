import math
def ceil(x):
    """arredonda para cima"""
    return math.ceil(x)
def carros(x,y=5):
    """n de carro necessario para viajem sendo x pessoas, y carros"""
    return ceil((x/y))