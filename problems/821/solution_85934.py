# Fatorial
def fatorial(n):
    '''Essa função retorna o fatorial de um número inteiro n;
    INT -> INT'''
    produto = 1
    i = 1
    while i in range(1,(n+1)):
        produto = produto * i
        i += 1
    return produto