import math
def carros (n,c=5):
    '''Dado o número de pessoas n e a capacidade de cada carro c, calcule quantos carros serão necessários para a viagem; int,int -> int'''
    return math.ceil(n/c)