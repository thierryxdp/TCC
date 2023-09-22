import math
def bolos(A,B,C):
    """função que calcula e retorna a quantidade de bolos que podem ser feitos por joão dadas as xícaras de farinha de trigo disponíveis A, a quantidade de ovos B
    e a quantidade de colheres de sopa de leite C como entradas; int, int, int ->int"""
    return min(A//2,B//3,C//5)