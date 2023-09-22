import math
def carros(amigos,capacidade=5):
    """ calcula e retorna o numero de carros"""
    return math.ceil(amigos/capacidade)