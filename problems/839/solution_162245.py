import math
def carros(passageiros,capacidade=5):
    """calcula e retorna a quantidade exata de carros necessários para a viagem, dados a quantidade de pessoas e caso não seja um carro convencional, a capacidade do veículo"""
    return math.max(passageiros//capacidade)