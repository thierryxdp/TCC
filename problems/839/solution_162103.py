import math 
def carros(P,Cp):
    '''fun que calcula a quantidade
    de carros necessarios para uma
    viagem dado a quantidade de pessoas 
    e da capacidade do carro'''
    return math.ceil(P/Cp)