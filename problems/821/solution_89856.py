def fatorial(n):
    '''
       Função que retorna o fatorial de n.
       int -> int
    '''
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    return f