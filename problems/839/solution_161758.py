import math
def carros(pessoas,capacidade=5):
    '''função que define quantos carros serão necessários'''
    return math.ceil  (pessoas/capacidade)