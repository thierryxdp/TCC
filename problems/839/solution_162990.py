import math 
def carros(pessoas, capacidade):
    '''numero de carros necessarios'''
    return math.ceil(pessoas//capacidade)