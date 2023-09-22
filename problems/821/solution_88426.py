def fatorial(n):
    '''acha o fatorial de um número
    int -> int'''
    proximo = n-1
    fatorial = n * proximo
    proximo = n-2
    while proximo >= 1:
        fatorial = fatorial * proximo
        proximo = proximo - 1
    return fatorial