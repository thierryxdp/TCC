def fatorial(n):
    '''Função que calcula o fatorial de um número:
    int -> int '''
    f=1
    i=2
    while i <= n:
        f = f*i
        i = i + 1
    return f