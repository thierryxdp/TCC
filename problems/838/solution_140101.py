import math

def num_bombons(x,y):
    '''Essa função determina a quantidade de bombons que podem ser comprados
    dados os valores de x (dinheiro) e y (preço do bombom)'''
    return math.ceil(x/y)