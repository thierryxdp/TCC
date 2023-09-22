def fatorial(n):
    '''acha o fatorial de um número
    int -> int'''
    if n == 1:
        return 0
    proximo = n-1
    fatorial = n * proximo
    proximo = n-2
    while proximo >= 1:
        fatorial = fatorial * proximo
        proximo = proximo - 1
    return fatorial