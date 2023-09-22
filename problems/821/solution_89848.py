def fatorial(n):
    '''Calcula o fatorial de um número.
    int -> int'''
    acc = n
    while n >= 1:
        n -= 1
        acc *= n
    return acc