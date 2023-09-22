import math

def bolos(a,b,c):
    '''define quantos bolos João conseguirá fazer com a xícaras de farinha de trigo, b ovos e c colheres de sopa de leite'''
    A=a/2
    B=b/3
    C=c/5
    x=min(A,B,C)
    return math.floor(x)