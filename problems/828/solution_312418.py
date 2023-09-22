from math import *

def primo(n):
    '''função que dado um inteiro, retorna True se este for primo e False se não for. int -> bool'''
    acumulador = 0
    for i in range(int(sqrt(n))):
        if i != 0:
            if n % i == 0:
                acumulador = acumulador + 1
    if acumulador == 0:
        return True
    else:
        return False