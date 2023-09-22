import math
def carros(y,x=5):
    '''Essa função calcula a quantidade de carros tendo como valor default para o numero de pessoas por carro 5'''
    h = y/x 
    return math.ceil(h)