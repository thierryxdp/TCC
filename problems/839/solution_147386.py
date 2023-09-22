def carros(x,y=5):
    """calcula a quantidade de veiculos para uma viagem;
    x(pessoas), y(capacidade); import math"""
    return math.ceil(x/y)