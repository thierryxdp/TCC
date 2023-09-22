import math
def carros(n,c=5):
    """funcao que dado o numero de pessoas n e o numero de assentos c em 
    determinado modelo de carro, determina quantos carros desse modelo
    serao necessarios para acomodar a quantidade de pessoas informada
    (se c não for informado, c=5)"""
    return math.ceil(n/c)