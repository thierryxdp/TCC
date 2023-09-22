import math
def carros( pessoas,capacidade=5):
    ''' funcao que retorna o o numero de carros para q quntidade de pessoas'''
    return math.ceil(pessoas/capacidade)