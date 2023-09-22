def fatorial(n):
    '''Funcao que calcula o fatorial de um dado
    numero n; int -> int'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i += 1
    return f