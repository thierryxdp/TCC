from math import *

def primo(n):
    '''função que dado um inteiro, retorna True se este for primo e False se não for. int -> bool'''
    contador = 0
    for i in range(int(sqrt(n)) + 1):
        if i >= 2:
            if n % i == 0:
                contador += 1
    if contador == 0:
        return True
    elif contador >= 1:
        return False