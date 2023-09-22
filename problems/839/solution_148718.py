import math
def carros(x,y=5):
    """funcao que calcula o numero necessarios de carros para uma viagem dado o numero de pessoas. Dados: x = numero de pesssoas e y= capacidade do carro"""
    return math.ceil(x/y)