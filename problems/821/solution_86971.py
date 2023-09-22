def fatorial(n):
    '''Funcao python que recebe um numero e retorna o
    fatorial desse numero (int -> int)'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat