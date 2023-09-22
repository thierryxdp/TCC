import math
def carros(p,c=5):
    '''dados o numero de pessoas (p) e, caso necessario, a capacidade do carro(c), retorna o numero de carros necessarios para transportar (p) pessoas;
    int, int -> int'''
    return math.ceil(p/c)