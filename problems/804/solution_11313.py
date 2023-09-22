from math import *

def filtra_pares(a):
    '''
    Dado uma tupla com quatro elementos inteiros retorna uma nova tupla

    Uso:
    filtra_pares(a)

    Entrada:
    - a (tupla, obrigatória): variavél 1

    Saída:
    - Uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    '''
    tupla = ()
    if x[0] % 2 == 0:
        tupla = tupla + (x[0],)
        if x[1] % 2 == 0:
            tupla = tupla + (x[1],)
            if x[2] % 2 == 0:
            tupla = tupla + (x[2],)
                if x[3] % 2 == 0:
                tupla = tupla + (x[3],)
    return tupla