import math
def carros(pessoas,capacidade=5):
    """calcula o número exato de carros necessários para
    uma viagem com determinado número de pessoas"""
    resultado = pessoas/capacidade
    return math.ceil(resultado)