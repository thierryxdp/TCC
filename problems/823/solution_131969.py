def faltante(L):
    """descobre o número que falta na lista
       list --> int"""
    i = 0
    list.sort(L)
    
    while i < len(L):
        if L[i] != i + 1:
            return L[i] - 1
        i += 1
    return L[-1] + 1