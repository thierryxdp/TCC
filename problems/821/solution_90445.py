def fatorial(n):
    """
    Essa função retorna o fatorial de um número ('n').
    int => int
    """

    i = 0
    f = 1
    n2 = n
    while i < n:
        f = f * n2
        n2 = n2 - 1
        i = i + 1
    return f