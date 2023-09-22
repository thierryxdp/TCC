from math import ceil 
def carros(P, Cp):
    '''funcao que calcula a quantidade 
    de carros necessarios para uma viagem
    dada a quantidade de pessoas e a 
    capacidade do carro'''
    return math.ceil(P/Cp)