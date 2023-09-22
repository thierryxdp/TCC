#Escreva sua função aqui. Pode apagar essa linha.
import math
def num_bombons(dinheiro, preço):
    """retorna a quantidade de bombons que podem ser comprados dado o dinheiro e o preço; float, float -> int"""
    return math.floor(dinheiro/preço)