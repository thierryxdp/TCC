def calcFatorial(n):
    '''Retorna o fatorial do número de entrada;
       int -> int'''
    fatorial=n
    while n-1!=0:
        fatorial=fatorial*(n-1)
        n=n-1
    return fatorial