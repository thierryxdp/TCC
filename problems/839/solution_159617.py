import math
def carros(pessoas,capacidade):
    '''função que define quantos carros são necessários para levar um grupo de amigos
    int, int -> int'''
    return math.ceil (pessoas/capacidade)