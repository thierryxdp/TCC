def filtraMultiplos(list, n):
    """..."""
    """list,int->list"""
    indice=0
    list = []
    while indice < len(list):
        if list[indice] % n == 0:
            return list
        
        indice = indice + 1
    return resposta