#2
'''
    Função que calcula a quantidade de carro necessaria uma
    viagem dado o numero de pessoas viajando (p) e a
    capacidade unica de passageiros dos carros (c),
    prioritariamente 5.
    int, int -> int
'''    
    
import math
def carros (p, c=5):
    return math.ceil (p/c)