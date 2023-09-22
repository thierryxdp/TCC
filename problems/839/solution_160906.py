import math 
def carros(pessoas,capacidade=5):
    """calcule e retorne o numero de carros dado a quantidade de pessoas e a capacidade de um veículo"""
    return math.ceil(pessoas/capacidade)