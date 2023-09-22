import math
def carros(x,y):
    """função que calcula e retorna a quantidade de carros necessários para a viagem, dados o números de pessoas x e capacidade do veículo y"""
    return math.ceil (x/y)