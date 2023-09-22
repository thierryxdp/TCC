def fatorial(n):
    """Função que dado um número calcula o fatorial do mesmo"""
    """int -> int"""
    i = n
    x = 1
    while i > 0:
        x = x * i
        i = i - 1
    return x