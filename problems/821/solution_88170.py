def fatorial(n: int)-> int:
    """Dado um número, a função retorna o fatorial deste número"""
    i = 1
    fatorial = 1
    while (i <= n):
        fatorial *= i
        i += 1
    return fatorial