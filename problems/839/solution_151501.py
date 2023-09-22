from math import*
def carros(p):
    '''calcular o numero de carros necessarios para transportar o numero de pessoas(p), sabendo que o limite para cada carro é de 5 pessoas'''
    return ceil(p/5)