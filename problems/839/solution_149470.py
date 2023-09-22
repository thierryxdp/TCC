import math
def carros(p,c=5):
    '''funcao para calcular a quantidade de carros para uma viagem dado nbumero de pessoas e assentos em cada carro'''
    return (math.ceil (p/c))