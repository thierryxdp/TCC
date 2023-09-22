from math import *
def bolos(A,B,C):
    '''função que calcula a quantidade de bolos que uma pessoa consegue fazer dados
    A(xícaras de farinha, B(ovos), C(colheres de sopa de leite)'''
    a=floor(A/2)
    b=floor(B/3)
    c=floor(C/5)
    return min(a,b,c)