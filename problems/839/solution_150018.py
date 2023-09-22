import math
def carros(p,c=5):
    """ função que calcula a quantidade de carro necessaria para uma viagem de até 5 pessoas
    levando em enconta que a capacidade do carro pode variar.
    p = passageiro
    c = carro"""
    return math.ceil(p/c)