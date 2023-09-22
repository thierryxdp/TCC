import math

def carros (passageiros, assentos):
    """ calcula a quantidade de carros necessários dado 
    o número de passageiros e a capacidade de cada carro. """
    if passageiros <= assentos:
        print (1)
    return math.ceil(passageiros//assentos)