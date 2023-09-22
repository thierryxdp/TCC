import math
def carros(pessoas,veiculos=5):
    """Calcula o numero de carros necessario para a viagem"""
    return math.ceil(int(pessoas//veiculos))