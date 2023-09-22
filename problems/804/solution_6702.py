def filtra_pares(tupla):
    """ função que recebe uma tupla composta por quatro elementos
        do tipo inteiro e retorna uma nova tupla contendo apenas
        os elementos pares da primeira
        tuple -> list """
    a,b,c,d = tupla
    if a % 2 == 0:
        return a
    if b % 2 == 0:
        return b