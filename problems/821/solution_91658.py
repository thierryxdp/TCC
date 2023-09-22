def fatorial (n):
    '''Função que calcula o fatorial de um número
    int -> int'''
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i = i+1
    return fat