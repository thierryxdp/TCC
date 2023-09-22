import math

def carros(pessoas,capacidade=5):
    '''função que dado o núm. de pessoas retorna quant. de carros'''
     
    return math.ceil(pessoas/capacidade)