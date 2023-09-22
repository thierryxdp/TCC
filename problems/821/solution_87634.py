def fatorial(x):    
    '''Calcula o fatorial de um número
    int ->int'''
    i = 1
    for n in range(2, x + 1):
        i = i * n
    return i