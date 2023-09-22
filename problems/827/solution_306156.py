def qtd_divisores(n):
    '''Função que recebe um numero n, e retorna quantos divisores n possui.'''
    ''' int/float -> int'''
    divisores = []
    for elementos in range(1, n+1):
        if n % elementos == 0:
            list.append(divisores, elementos)
    return len(divisores)