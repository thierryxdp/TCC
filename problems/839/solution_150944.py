from math import *
def n_carros (p,c=5)
	"""calcula e retorna o número mínimo de veículos necessários para realizar uma
    viagem dados o número total "p" de passageiros e a capacidade "c" dos veículos.
    Se nenhuma capacidade de passageiros for inserida "c" será considerada como 5;
    int,int->int"""
    return ceil p/c