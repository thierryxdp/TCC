import math
def carros (passageiros, capacidade=5):
    return math.ceil(passageiros/capacidade)
'''funcao que calcula quantos carros sao necessarios 
para uma determinada viagem
int,int->int'''