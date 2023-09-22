from math import *
def bolos(a,b,c):
    '''retorna a quantidade de bolos que João consegue fazer
    dados os ingredientes: (a)xícaras de farinha, (b)ovos e
    (c)colheres de sopa de leite'''
    if b == 0:
        return a
    else:
        return mdc(b, a%b)