import math

def bolos(a,b,c):
    '''Calcula o maximo de bolos inteiros que joao conseguira fazer dados o 
    numero de xicaras de farinha "a", o numero de ovos "b" e colheres de sopa 
    de leite "c";int||float,int||float->int'''
return math.floor(min(a/2,b/3,c/5)