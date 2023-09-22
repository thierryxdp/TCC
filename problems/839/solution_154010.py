import math
def carros(n,c=5):
    """Funcao que calcula o numero de carros necessarios, dado numero de pessoas(n) e capacidade do veiculo(c)"""
    return math.ceil(n/c)