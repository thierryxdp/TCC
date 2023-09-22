def qtd_divisores(numero):
    """."""
    contador = 0
    for numero in range(numero):
        if numero%(numero+1) == 0:
            contador = contador + 1
    return contador