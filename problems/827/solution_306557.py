def qtd_divisores(n):
    '''Retorna a quatidade de divisores de um número.
    int -> int'''
    acc = 0
    for i in range(n):
        if n % i == 0:
            acc += 1
    return acc