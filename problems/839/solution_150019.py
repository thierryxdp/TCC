import math
def carros(cp,c=5):
    """ função que calcula a quantidade de carro necessaria para uma viagem de até 5 pessoas
    levando em enconta que a capacidade do carro pode variar.
    cp = capacidade do carro 
    np = numero de pessoa"""
    return math.ceil(cp/np)