import math
'''Definir quantos carros são necessarios para a viagem'''
'''int,int->int'''
def carros (x, y):
    return  math.ceil(x / y)