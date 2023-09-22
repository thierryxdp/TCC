import math 
def carros(p,c=5):
    '''função que calcula e retorna a quantidade necessária de veículos para transportar p pessoas,baseada na capacidade c'''
    return math.ceil(p/c)