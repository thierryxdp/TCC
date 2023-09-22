import math
def carros(pessoas,capacidade=5):
    """Funcao que calcula o numero exato de carros necessarios para transportar a quantidade de pessoas desejadas"""
    return math.ceil(pessoas/capacidade)