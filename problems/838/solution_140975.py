import math

def num_bombons(d,p):
    '''função para calcular o número de bombons que podem ser comprados
    com d reais, sendo o preço unitário p
    float, float -> int'''
    return math.floor(d/p)