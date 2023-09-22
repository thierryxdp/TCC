def fatorial(n):
    ''' Calcula o fatorial de N.
    int -> int '''
    f = 1
    i = n * (n -1)
    while n >= 1:
        f = f * n
        n = n - 1
    return f