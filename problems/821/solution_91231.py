def fatorial(n):
    ''' Função em que calcula o fatorial
     	de um numero inteiro.
        int--->int'''
    i=1
    valor=1
    while valor<=n:
        valor= valor*n
        i= i+1
    return valor