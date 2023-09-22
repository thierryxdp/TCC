def qtd_divisores(numero):
    """."""
    y = 0
    for x in range(numero):
        if numero%x == 0:
            y = y + 1
    return y