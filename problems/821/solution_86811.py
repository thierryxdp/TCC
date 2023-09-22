def fatorial(n):
    '''Recebe um numero e retorna o fatorial dele.
    int -> int'''
    i = 1
    fat = 1
    while i <= n:
        fat = fat * i
        i += 1
    return fat