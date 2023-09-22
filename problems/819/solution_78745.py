def filtraMultiplos(lista, x):
    """..."""
    i = 0
    novalista = []
    while i <= len(lista)-1:
        if lista[1] % x == 0:
            novalista.append(lista[i])
            
         i += 1
    return novalista