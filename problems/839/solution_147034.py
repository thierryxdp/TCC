import math
def carros(pessoas, capacidade=5):
    """retorna o número de carros necessários para uma viagem, dado o número de pessoas e a capacidade do veículo, sendo que um veículo convencional tem capacidade para 5 pessoas; int, int -> int"""
    return math.ceil(pessoas/capacidade)