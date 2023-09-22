import math
def carros(p,l=5):
    '''Retorna o numero de carros para transportar
    p passageiros. Padrao de 5 lugares por carro;
    int, int -> int'''
    return math.ceil(int(p/l))