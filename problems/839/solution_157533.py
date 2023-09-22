import math

def carros (pessoas,capacidade=5):
    '''recebe a quantidade de pessoas e a capacidade dos carros e 
retorna o numero de carros necessários, int,int=int'''
    return math.ceil(pessoas/capacidade)