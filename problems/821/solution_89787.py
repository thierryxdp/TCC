def fatorial(n):
    ''' calcula o fatorial de um número sem usar o módulo math;
    int -> int '''
    i=1
    fatorial=1
    while i <= n:
        fatorial=fatorial*i
        i=i+1
    return fatorial