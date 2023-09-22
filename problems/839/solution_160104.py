import math
def carros (x):
    """define quantos carros serao necessarios para fazer
    uma viagem, sendo x o numero de pessoas
    int -> int"""
    return math.ceil((x/5))