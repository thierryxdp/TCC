import math
def bolos(farinha,ovos,leite):
   """define o numero maximo de bolos a serem feitos com os ingredientes fornecidos dividindo esses pela quantidade necessaria de cada um para um bolo; int, int, int-> int"""
    nfarinha = (farinha//2)
    novos = (farinha//3)
    nleite = (leite//5)
    nbolos = min(nfarinha,novos,nleite)
    return nbolos