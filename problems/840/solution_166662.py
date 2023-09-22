import math
def bolos (a, b, c):
    '''funcao que calcula a quantidade maxima e bolos que joao  consegue fazer dado valores min de ingredientes para cada bolo;
    float,float,float -> int'''
    return min (a//2, b//3, c//5)