import math

def carros(p,c=5):
    """retorna a quantiadade de carros necessários para carregar p pessoas, sendo a capacidade de cada veículo sendo c"""
    return math.ceil(p/c)