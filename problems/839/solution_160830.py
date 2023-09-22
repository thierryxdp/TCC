import math
"""calcula quantos carros(y) são necessários para levar um número x de pessoas, 
se a capacidade do carro não for informada, o valor considerado será 5."""
def carros(p,c=5):
    return math.ceil(p/c)