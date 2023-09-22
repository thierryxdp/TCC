import math

#Função que calcula a quantidade máxima de bolos que João conseguirá fazer dados os ingredientes
#A = xícaras de farinha, B = ovos e C = colheres de leite

def bolos(A,B,C):
    """calcula a quantidade máxima de bolos que João fará;
    int/float, int, int/float"""
    return int(min((A//2),(B//3),(C//5)))