def fatorial(n):
    '''A função recebe um número n e retorna o fatorial de n.
    Parâmetro de entrada: int
    Valor de retorno: int'''
    fatorial=n
    i=1
    while i<n:
        n=n-1
        fatorial=fatorial*n
    return fatorial