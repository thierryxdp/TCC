def filtra_pares(tuplas):
    """retorna apenas os elementos pares de uma tupla na ordem em que se encontram."""
    pares=()
    if (tuplas[0]%2)==0):
        pares+=(tuplas[1],)
    return pares