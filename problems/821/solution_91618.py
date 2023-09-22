def fatorial(n):
    '''Calcular o fatorial de n.
    int -> int'''
    total = 1
    while n == total:
        total = total * (n + 1)
    return total