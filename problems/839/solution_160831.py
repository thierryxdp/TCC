import math
def carros(p,c=5):
    """Retornar o número de carros possíveis para o transporte; int, int =>int"""
    return math.ceil(p/c)