def fatorial(n):
    ''' Função que calcula o fatorial de um numero sem usar a função do
    modulo math.          int=>int'''
    i = 1
    k = 1
    lista = list()
    while i <= n:
        k=k*i
        i=i+1
    return k