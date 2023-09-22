from math import*
def carros(p,cdc=5):
    """Calcula a quantidade de carros necessário para transportar uma quantidade de p de pessoas, caso não informado a capacidade do carro sera 5"""
    return ceil(p/cdc)