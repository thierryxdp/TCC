def fatorial(n):
    '''Recebe um número n e retorna o fatorial desse número; int -> n'''
    i = 2
    fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat