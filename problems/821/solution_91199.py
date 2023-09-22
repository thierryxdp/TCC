def fatorial(n):
    """
    Essa função dado como argumento um numero inteiro positivo,
    ira retornar o fatorial deste numero.
    inte->float
    """
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)