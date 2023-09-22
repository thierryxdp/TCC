#Calcula quantos carros é necessário para transportar um número p de passageiros.
import math

def carros(p,v=5):
    capacidade=p/v
    return math.ceil(capacidade)