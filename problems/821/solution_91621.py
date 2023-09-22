def fatorial(n):
    '''Calcular o fatorial de n.
    int -> int'''
    total = 1
    i = 2
    while i <= n:
        total = total * i
    i = i + 1
    return total