import math
def carros(p, c=5):
    '''Calcula e retorna o numero de carros necessarios para uma viagem, 
     dados o numero de passageiros (p) e a capacidade maxima do carro (c);
     int, int -> int'''
    return math.ceil(p/c)