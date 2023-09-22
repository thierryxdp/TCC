import math
def carros(p,v=5):
    """ retorna o numero de veiculos necessarios para uma determinada viagem dados os numeros de pessoas(p) e capacidade do veiculo(v) """
    return math.ceil(p/v)