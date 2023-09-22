import math
def carros(n,y=5):
    """ calcula e retorna o numero de carros necessarios para fazer a 
    viagem, sendo n o numero de pessoas e y a capacidade de um carro;
    x=int,y=int->int"""
    return math.ceil (n/y)