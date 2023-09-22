from math import *
def carros (x,y=5):
    """Função que calcula o número de carros para uma viagem dado o número de passageiros (x) e número de assentos de carro não convencional (y)"""
    return (ceil(x/y))