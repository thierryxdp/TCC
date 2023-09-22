import math

def num_bombons(saldo, valor):
    """calcula quantos bombons se pode comprar
    custando um valor definido,
    com o saldo disponível"""
    return math.floor(saldo/valor)