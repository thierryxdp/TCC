import math 
def carros(pessoas, capacidade=5):
    '''quantidades de carros necesssarios'''
    return math.ceil (pessoas/capacidade)