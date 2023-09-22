import math
def carros (p,c=5):
    '''recebe o número de pessoas (p) e a capacidade dos veículos (c) e retorna o número de veículos necessários (caso a capacidade não seja dada, o valor atribuído será automaticamente "5")'''
    return math.ceil (p/c)