import math

def num_bombons(x,y):
    """funcao que calcula o quantos bombons se consegue comprar, no maximo, a partir de dados
    como: dinheiro(x) e preço da unidade do bombom(y)"""
    return math.floor(x/y)