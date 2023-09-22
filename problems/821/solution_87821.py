def fatorial(x):
    '''Calcula o Fatorial de um número. int -> int'''
    i = x
    f = x
    while i != 1:
        f = f*(i-1)
        i = i - 1
    return f