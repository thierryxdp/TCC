def fatorial(n):
    '''
    A função retorna o fatorial de um número
    (entrada = int / saída = int)
    '''
    i = 1
    n1 = n
    while i == n:
        n1 = n1 * (n1 - i)
        i = i - 1
    return n1