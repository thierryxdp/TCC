import math
def carros (passageiros,capacidade=5):
    """Retorna a quantidade de carros necessária para transportar certo número de passageiros considerando o número de vagas do veículo"""
    return math.ceil(passageiros/capacidade)