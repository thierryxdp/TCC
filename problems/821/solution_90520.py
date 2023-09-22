def fatorial(n):
    """ Dado um número n de entrada, calcule o fatorial deste númrero"""
    i = 1
    fat = 1
    while (i<=n):
        fat = fat*i
        i=i+1
    return fat