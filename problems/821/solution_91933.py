def fatorial(x):
    """calcula o fatorial de um valor dado
    int -> int
    """
    f = 1
    for c in range(x, 0, -1):
        f *= c
    return f