import math
def bolos(A,B,C):
    '''restona o numero de bolos possíveis de fazer com, dados A(Xícaras
    de farinha), B(numero de ovos), C(colheres de sopa de leite)'''
    return min(A//2,B//3,C//5)