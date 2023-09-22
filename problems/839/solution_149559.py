import math
def carros (pessoas,carro=5):
    """funcao que calcula quantos carros sao necessarios de acordo com o numero de pessoas que vai na viagem
    int -> int"""
    return math.ceil(pessoas/carro)