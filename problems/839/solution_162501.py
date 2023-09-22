import math
def carros(p,c=5):
    """Define uma função que calcula o número de carros 
    necessários para p (passageiros), com um carro de 
    c (capacidade de lugares)
    int,int->int"""
    return math.ceil p/c