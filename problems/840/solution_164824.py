import math

def farinha(A):
    """função que calcula e retorna a quantidade de receitas de bolo que João pode fazer
    com o número de xícaras de farinha de trigo que João possui em casa; int -> int"""
    return A//2


def ovos(B):
     """função que calcula e retorna a quantidade de receitas de bolo que João pode fazer
     com o número de ovos que João possui em casa; int -> int"""
     return B//3


def leite(C):
    """função que calcula e retorna a quantidade de receitas de bolo que João pode fazer,
    com o número de colheres de sopa de leite que João possui em casa; int -> int"""
    return C//5

   
def bolos(A,B,C):
    """função que calcula e retorna o número de bolos que podem ser feitos por João,
    através do valor mínimo do retorno das funções farinha, ovos e leite, através
    dos valores de entrada A,B e C, respectivamente xícaras de farinha de trigo,
    ovos e colheres de sopa de leite; int, int, int -> int"""
    return min(farinha(A), ovos(B), leite(C))