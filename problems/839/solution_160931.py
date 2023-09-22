from math import *
def carros (p,c=5):
    """calcula e retorna o número de carros necessários dado um número p de pessoas e um valor c da capacidade dos carros, caso esta não seja dada será considerada a capacidade de um veículo convencional, 5 pessoas por carro"""
    return round(p//c)