import math
def carros(p):
    '''função que retorna o número de carros necessários para transportar p pessoas
    int -> int'''
    return math.ceil(p/5)