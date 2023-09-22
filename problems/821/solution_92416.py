def fatorial(n):
    '''Dado um número, retorna o fatorial deste número
    int -> int'''
    t=n
    i=0
    fatorial=1
    while i <n:
        fatorial=fatorial*t
        t=t-1
        i+=1
    return fatorial