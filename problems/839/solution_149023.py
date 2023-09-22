import math
def carros(p,c=5):
    '''Calcula o numero de carros necessarios para uma viagem dado o numero n de pessoas,
    e a capacidade c de passageiros por carro, se nao for informado a capacidade, adotora 5 como valor padrao
    int, int -> int'''
    return math.ceil(p/c)