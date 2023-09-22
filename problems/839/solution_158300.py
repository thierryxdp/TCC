import math
def carros (pessoas, assentos = 5):
    '''Calcula quantos carros são necessários para fazer uma viagem.
       int, int -> int'''
    return math.ceil (pessoas, assentos)