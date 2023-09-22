import math
def carros (n:int , c = 5) -> int:
    """dividindo n por c, sendo n o número de pessoas e c a capacidade do carro, temos
    a quantidade necessaria de veiculo"""
    return math.floor (n/c)