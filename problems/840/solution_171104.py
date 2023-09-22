import math
def bolos(farinha,ovos,leite):
   """define a quantidade de bolos a serem feitos com os ingredientes fornecidos sendo a quantidade de farinha em xicaras e a de leite em colheres de sopa; int, int, int-> int"""
    nbolos = min(farinha//2, ovos//3, leite//5)
    return nbolos