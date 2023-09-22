import math
def carros(p,c=5):
    """Define uma função que calculo o número de carros 
    necessários para p (passageiros), com um carro de 
    c (capacidade de lugares)"""
    return math.ceil p//c