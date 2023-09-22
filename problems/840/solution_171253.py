from math import *
def bolos (A,B,C):
    """calcula e retorna o número de bolos  que podem ser feitos seguindo a receita de 2 xícaras
de farinha de trigo, 3 ovos e 5 colheres de sopa de leite, sendo A a quantidade de xícaras de farinha de trigo disponíveis; B, a de ovos; e C, a de colheres de sopa de leite"""
    return min(floor(A/2,B/3,C/5))