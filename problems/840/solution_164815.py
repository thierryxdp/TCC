import math
def bolos(A,B,C):
    '''Calcula o maximo de bolos inteiros que joao conseguira fazer dados o 
    numero de xicaras de farinha "A", o numero de ovos "B" e colheres de sopa 
    de leite "C";int||float,int||float->int'''
return math.floor(min(A/2,B/3,C/5))