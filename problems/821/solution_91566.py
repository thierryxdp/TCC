def fatorial(n):
    """Essa função retorna o fatorial de um número 'n'
    int -> int"""
    l = n
    m = n
    while n>0:
        m = m*n
        n = n-1
    return m/l