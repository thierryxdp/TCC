from math import *
def soma():
    '''Função que calcula a soma dada 
    saida:float'''
    S = 0
    sinal = 1
    for i in range(1,11):
        S = S + sinal*(11-i)/factorial(i)
        sinal = sinal*(-1)
    return round(S,2)