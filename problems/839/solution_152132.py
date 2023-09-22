import math

def carros(p,c=5):
    """dado o número de pessoas de um grupo de amigos p e a capacidade do carro c,
     função retorna a quantidade de carros necessários para a viagem;
     int->int"""
    return math.ceil(p/c)