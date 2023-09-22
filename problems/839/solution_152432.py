import math
def carros(pessoas,veiculos=5):
    """calcula o numero de carros para levar as pessoas na viagem
    int->int"""
    return math.ceil(pessoas/veiculos)