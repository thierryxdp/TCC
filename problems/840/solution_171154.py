import math

def bolos(A,B,C):
    '''funcao que calcula a quantidade maxima de bolos que Joao consegue fazer
    com a quantidade de ingredientes disponiveis, sendo respectivamente, o
    numero de xicaras de farinha de trigo, o numero de ovos e o numero de
    colheres de sopa de leite
    :param A: int
    :param B: int
    :param C: int
    :return: int
    '''

    return min(A//2,B//3,C//5)