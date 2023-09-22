import math
def arrendodamento(x):
    """Função que retorna o numero dado como 
    entrada arrendodado para cima e inteiro float -> int"""
    return math.ceil(x)

def carrosViagem(pessoas,capacidade=5):
    """Função que calcula e retorna o número exato de carros
    necessários para uma viagem dados o número de pessoas;
    int, int -> int"""
    return math.ceil(pessoas/capacidade)