def qtd_divisores(n):
    ''' Retorna quantos divisores(int) um número n(int) tem. '''
    n_div = 0
    for x in range(1,n):
        if n % x == 0:
            n_div += 1
    return n_div