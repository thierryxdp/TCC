import math

def carros (passageiros, assentos):
    """ calcula a quantidade de carros dado o número de 
    passageiros e a capacidade de cada carro e retorna o
    número de carros."""
    if passageiros <= assentos:
        print (1)
    return round passageiros//assentos