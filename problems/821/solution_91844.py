def fatorial (n):
    '''Calcula o fatorial de um número n
    int -> int'''
    x = 1
    mult = n
    while x < n:
        mult = mult * x
        x = x + 1
    return mult