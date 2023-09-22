import math

def num_bombons(din,prec):
    '''Função que retorn a quantidade de bombons que podem ser comprados com o dinheiro
    informado.
    float ou int, float ou int -> int'''
    return math.floor(din/prec)