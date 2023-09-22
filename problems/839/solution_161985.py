import math as m
def carros(n,cap=5):
    '''função que define o número de carros necessários para n pessoas viajarem em carros de capacidade cap'''
    return m.ceil(n/cap)