import math
def carros (x,y==5):
    """define quantos carros serao necessarios para fazer
    uma viagem, sendo x o numero de pessoas e y a capacidade
    do veiculo
    int -> int"""
    return math.ceil((x/y))