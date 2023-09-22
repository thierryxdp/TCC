import math
def carros(pessoas, capacidade=5):
    '''função que define quantos carros são necessários para levar um grupo de amigos
    int, int -> int'''
    return math.ceil (pessoas/capacidade)