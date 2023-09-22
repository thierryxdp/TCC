import math
def carro(pessoas,capacidade = 5):
    """Calcular e retornar o número exato de carros necessário
    para esta viajem.
    int->int
    """
    return math.ceil(pessoas/capacidade)