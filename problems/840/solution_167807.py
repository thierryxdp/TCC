import math
def bolos(A,B,C):
    '''função que recebe a quantidade de xícaras de trigo(A), ovos(B)
    e colheres de sopa de leite(C) João possui e retorna quantos bolos
    ele poderá fazer; int,int,int->int'''
    return min(int(A/2,B/3,C/5))