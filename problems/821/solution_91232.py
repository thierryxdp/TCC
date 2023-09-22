def fatorial(n):
    ''' Função em que calcula o fatorial
     	de um numero inteiro.
        int--->int'''
    i=1
    valor=1
    while valor<=n:
        i=i*valor
        valor= valor+1
    return i