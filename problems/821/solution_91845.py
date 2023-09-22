def fatorial (n):
    '''Calcula o fatorial de um número n
    int -> int '''
    x = n - 1
    mult = n
    while x > 0:
        mult = mult * x
        x = x - 1
    return mult