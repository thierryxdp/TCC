def filtra_pares(tupla):
    """..."""
    a = []
    if tupla[0:]%2 == 0:
        a = a + tupla[0:]
    return a