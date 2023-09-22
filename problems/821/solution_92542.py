def fatorial (n):
    """Dado um número, calcula o fatorial deste número.
    assinatura: int--> int
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        return f