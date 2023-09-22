def carros (pessoas,assentos=5):
    """calcula e retorna o numero exato de carros necessarios para viagem, dado o numero de pessoas e a quantidade de assentos."""
    import math
    return math.ceil(pessoas/assentos)