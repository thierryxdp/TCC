def qtd_divisores(n):
    '''Funcao que conta o numero de divisores de um determinado numero'''
    i = 0
    for i in range (1, n//2+1):
        if n % i == 0:
            return i
        return n