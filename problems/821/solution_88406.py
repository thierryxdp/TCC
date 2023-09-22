def fatorial(n):
    '''Função que calcula fatorial
    float -> float'''
    i = 1
    fatorial=1
    while i <= n:
        fatorial = fatorial*i
        i = i + 1
    return fatorial