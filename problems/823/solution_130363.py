def faltante(L):
    """Retorna o numeoro faltante na lista dada como entrada
    list -> int"""
    
    n = len(L)
    i = 0
    
    while i < n:
        if i not in L:
    		return i
        i = i + 1