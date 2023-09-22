import math
def carros (a,b=5):
    '''Função que retorna o numero de carros necessarios pra para viagem
int, int -> int'''
    return math.ceil(a/b)