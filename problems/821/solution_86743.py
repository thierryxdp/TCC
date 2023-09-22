def fatorial(n):
    '''Função que recebe um número e retorna o cálculo do fatorial dele; int - > int'''
    cont = 1
    result = n
    while cont != n:
        result = result * (n-1)
        n = n-1

    return result