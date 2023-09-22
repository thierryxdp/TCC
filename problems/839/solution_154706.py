from math import *
def carros(pessoas,capacidadeDoVeiculo=5):
    """Dado o número de pessoas que irá na viagem e a capacidade de
    pessoas por veículos, a função calcula a quantidade de carros 
    necessarios para realizar a viagem e o retorna.
    Parametros de Entrada: int,int;
    Retorna:int"""
    return ceil(pessoas/capacidadeDoVeiculo)