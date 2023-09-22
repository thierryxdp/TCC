import math
def carros(p,c=5):
    '''calcular quantos carros sao necessarios numa viagem, sendo que cada carro so pode ter 5 pessoas'''
    return math.ceil(p/c)