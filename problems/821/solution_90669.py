def fatorial(numero):
    '''Função que dado um numero de entrada, calcula o
fatorial desse numero;
    int -> int'''
    fatorial=1
    n=1
    while n <= numero:
        fatorial=fatorial*n
        n=n+1
    return fatorial