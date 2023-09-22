import math
def carros(pessoas,capacidade=5):
    """calcula e retorna a quantidade de carros necessárias
    em função da quantidade de pessoas e da capacidade de 
    cada veículo
    int, int -> int"""
    return math.ceil(pessoas/capacidade)