import math
def carros(p,cap=5):
    '''Calcula a quantidade de veículos necessários para uma viagem com 'p' pessoas tendo a capacidade;
    int,int -> int'''
    return round(math.ceil(p/cap))