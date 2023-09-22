def fatorial(n):
    '''Função que retorna o fatorial do número, dado um número n; int->int'''
    fatorial=1
    while n>0:
        fatorial=fatorial*n
        n=n-1
    return fatorial