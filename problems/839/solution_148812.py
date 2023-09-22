import math
def carros(p,c=5):
    """ função que calcula o número de carros necessários para transportar um número p de passageiros de acordo com a capacidade c de cada veículo """
    return math.ceil(p/c)