def filtraMultiplos(L, n):
    """..."""
    """list,int->list"""
    indice=0
    lista = []
    while indice < len(L):
        if L[indice] % n == 0:
            list.append(lista, L[indice])
        
        indice = indice + 1
    return lista