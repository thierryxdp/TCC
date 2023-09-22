def soma_h(h):
    """
    Realiza a soma de uma determinada p.a.
    int -> float
    """
    i = 0
    x = 0
    while i <= h:
        x += 1/(1*i + 1)
        i += 1

    return x