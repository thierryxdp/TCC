from math import math.ceil
def carros(p,v=5):
    """ Define a quantidade exata de carros necessários para realizar uma viagens
    p = número total de pessoas
    v = número máximo de pessoas por carro ( deafult = 5 )"""
    return math.ceil(p/v)