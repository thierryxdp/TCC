import math
def bolos(A,B,C):
    '''Função que calcula o máximo de bolos a partir da quantidade de cada ingrediente; int, int, int->int'''
x= A//2
y= B//3
z= C//5
if x<=y and x<=z:
    return x
elif y<=x and y<=z:
    return y
elif z<=x and z<=y:
    return z