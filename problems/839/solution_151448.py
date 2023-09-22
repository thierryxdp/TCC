from math import *

def carros(p,c=5):
    '''função que calcula a quantidade de carros necessários para levar uma quantidade de pessoas(p) sobre a capacidade do carro(c); int, int -> float'''
    return ceil(p/c)