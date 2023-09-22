from math import *
def bolos(A,B,C):
    """função que retorna a quantidade de máxima de bolos que se pode fazer com base na receita dados A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite"""
    d=(A//2,B//3,C//5)
    return gdc(d)