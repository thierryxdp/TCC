import math

def carros(pessoas,veiculos=5):
    """funcao que calcula a quantidade de carros necessarios para viagem,dado o numero de pessoas e a capacidade do veiculo ,mesmo sendo de capacidade não convencional"""
    return math.ceil(pessoas//veiculos)