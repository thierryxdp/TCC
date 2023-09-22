import math
def quant_carros(p,c=5):
    "Calcula quantos carros são necessários para levar p pessoas, tendo como default5 de capacidade"
    carro=p/c
    return math.ceil(carro)