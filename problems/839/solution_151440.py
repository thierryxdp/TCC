from math import ceil

def carros(p, c = 5):
    '''Função que calcula o número de veículos necessários para uma viagem de p pessoas (p >= 0),
	com automóveis com capacidade c (c > 0), se o parâmetro c não for dado c = 5'''
    return ceil(p // c)