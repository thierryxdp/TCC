def fatorial(n):
    '''funcao que calcula o fatorial de um numero'''
    fatorial = 1
    indice = 2
    while indice <= n:
        fatorial = fatorial * indice
        indice = indice + 1
    return fatorial