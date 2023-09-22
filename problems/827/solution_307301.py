def qtd_divisores(numero):
    """."""
    contador = 0
    for x in range(numero):
        if numero%(x+1) == 0:
            contador = contador + 1
    return contador