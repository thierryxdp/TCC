def fatorial(n):
    """Dado um numero n, calcula o seu fatorial
    int -> int"""
    a = 1
    while n > 1:
        a = a*n
        n = n - 1
    return a