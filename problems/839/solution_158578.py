import math
def carros(pessoas,capacidade=5):
    '''função que define quantos carros um grupo de amigos precisam para fazer uma viagem
    int, int -> int.'''
    return math.ceil(pessoas/capacidade)