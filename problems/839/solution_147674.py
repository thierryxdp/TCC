import math
def carros (pessoas,capacidade=5):
    """Para calcular, e retornar, o número exato de carros necessários para fazer uma viagem,
    de acordo com o número de pessoas para viajar"""
    return math.floor(pessoas/capacidade)