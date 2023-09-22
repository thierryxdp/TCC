def fatorial(n):
    '''Função que retorna o fatorial de um número, dado o número n;nt->int'''
    fatorial=1
    while n!=0:
        fatorial=fatorial*n*(n-1)
        n=n-2
    return fatorial