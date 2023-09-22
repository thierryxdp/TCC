def filtra_pares(tupla):
    """..."""
    a = []
    if tupla[0]%2==0:
        a = a + tupla[0]
    elif tupla[1]%2==0:
        a = a + tupla[1]
    elif tupla[2]%2 == 0:
        a = a + tupla[2]
    elif tupla[3]%2==0:
        a = a + tupla[3]
        return a