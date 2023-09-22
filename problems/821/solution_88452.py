def fatorial(n):
    '''Calcula e retorna o fatorial de um número dado(n).
    int-->int'''
    i=1
    valor=1
    while i<=n:
        valor=valor*i
        i=i+1
    return valor