import math
def carros(p,c=5):
    """calcula e retorna o numero p de pessoas divido pela capacidade c, caso n dado o c sera usado o valor 5"""
    return math.ceil(p/c)