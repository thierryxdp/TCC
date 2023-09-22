def fatorial(n):
    '''dado um número n, retorna o fatorial desse número;
    int --> int'''
    lista = list(range(1,n+1))
    i = 0
    n = 1
    while i < len(lista):
        n = lista[i]*n
        i = i + 1
    return n