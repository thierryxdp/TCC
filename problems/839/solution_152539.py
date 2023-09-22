from math import*
def carros(pessoas,capacidade=5):
    '''retorna o numero de carros necessarios para viajar de
    acordo com numero de pessoas e capacidade de transportar
    int, int -> int'''
    return ceil(pessoas/capacidade)