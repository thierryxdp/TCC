import math
def carros (p, c = 5)
"""Calcula quantos veículos são necessários para transportar um número p de passageiros, em caso de veículo com outra capacidade que não 5, informar a seguir"""
return math.ceil (p/c)