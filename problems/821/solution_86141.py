def fatorial(n):
    """Pede um número n e calcula o fatorial desse número
    int->int"""
    fatorial = 1
    while n > 0:
        fatorial = fatorial*n
        n = n - 1
    return fatorial