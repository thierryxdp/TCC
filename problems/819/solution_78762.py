def filtraMultiplos(list, n):
    """..."""
    """list,int->list"""
    indice=0
    lista = []
    while indice < len(list):
        if list[indice] % n == 0:
            list.append(lista, list[indice])
        
        indice = indice + 1
    return lista