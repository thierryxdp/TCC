import math
def carros(p, c = 5):
    """ Dados o número "p" de passageiros
    e a capacidade "c" dos carros, calcula
    o número de carros necessários para 
    transporta os passageiros
    int, int -> int"""
    return math.ceil(p/c)