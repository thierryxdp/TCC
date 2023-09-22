def fatorial(n):
    """Função que dado um número n, calcula e retorna o
    fatorial deste número;
    int -> int"""
    n_fatorial = n
    while n != 1:
        n_fatorial = n_fatorial * (n - 1)
        n = n - 1
    return n_fatorial