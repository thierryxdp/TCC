import math
def carros (p,c=5):
    """Retorna o número necessário de carros para uma viagem dado o número de pessoas e a capacidade dos carros respectivamente"""
    return math.ceil(p/c)