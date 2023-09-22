import math
def carros(p,c=5):
    "Calcula quantos carros são necessários para levar p pessoas, tendo como default5 de capacidade"
    carros=p/c
    return math.ceil(carros)