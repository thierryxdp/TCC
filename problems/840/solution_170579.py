import math as m

def farinha(A):
    return m.floor(A/2)

def ovos(B):
    return m.floor(B/3)

def leite (C):
    return m.floor(C/5)

def bolos (A,B,C):
    '''
    	Parametros: (A,B,C) int.
        A = numero de xicaras de farinha de trigo.
        B = numero de ovos.
        C = numero de colheres de sopa de leite.
        Return: int.
    '''
    return ((20/100)*farinha(A))+((30/100)*ovos(B))+((50/100)*leite(C))