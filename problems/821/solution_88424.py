def fatorial(n):
    '''acha o fatorial de um número
    int -> int'''
    proximo = n-1
    fatorial = n * proximo
    while proximo >= 1:
        fatorado = proximo * proximo - 1
        fatorial = fatorial + fatorado
        proximo = proximo - 1
    return fatorial