eh_quadrada(m):
    """funcao que dada a matriz ela retorna true se for quadrada e false se nao for.
    list-->bool."""
    if len(m)==len(m[0]):
        return True
    else:
        return False