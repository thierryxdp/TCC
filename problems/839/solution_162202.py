import math
def carros(pessoas,capacidade=5):
    '''funcao que calcula o numero de carros para levar determinada quantidade de pessoas'''
    return math.ceil(pessoas/capacidade)