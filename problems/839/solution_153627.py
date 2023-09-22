import math

def carros(p, z=5):
    '''Retorna o numero de carros necessarios para fazer uma viagem, dado o numero de pessoas, sendo que cada carro suporta até 5 pessoas'''
    '''int ---> int'''
    return math.ceil(p/z)