def filtraMultiplos(lista, n):
    """ """
    lista = []
    indice = 0
    
    while lista[indice] % n == 0:
        indice = indice + 1
    return lista