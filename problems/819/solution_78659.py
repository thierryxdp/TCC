def filtraMultiplos(list, n):
    """..."""
    """list,int->list"""
    indice=0
    retorno=list
    while indice < len(list):
        if list[indice] % n == 0:
            list.append(list[indice], retorno)
    
        indice = indice + 1
    return retorno