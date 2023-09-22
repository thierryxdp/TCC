import math

def carros(pessoas, capacidade=5):
    """Retorna o número de veículos necessários para transportar
    um determinado número de pessoas de acordo com a capacidade
    deles. A capacidade padrão é de 5 passageiros por veículo.
    int, int -> int"""
    return math.ceil(pessoas / capacidade)