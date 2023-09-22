def fatorial(x):
    """Retorna o fatorial de um número.
    Entrada: int
    Saída: int
    """
    if x <= 1:
        return 1
    else:
        return x*fatorial(x-1)