def carros(p,c=5):
    """Função que calcula e retorna a quantidade exata de carros necessários para essa viagem, sendo p para número de pessoas e c para capacidade do carro"""
   import math
    return math.ceil(p/c)