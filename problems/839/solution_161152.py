import math

def	carros(p,l=5):
    """ calcular e retornar a o valor exato da quantidade de carros para um grupo de pessoas realizar uma viagem,considerando a capacidade do carro =5 pessoas """
    return math.ceil(p/l)