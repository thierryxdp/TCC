def faltante(L):
    """Retorna o numeoro faltante na lista dada como entrada
    list -> int"""
    
    i = 0
    
    while i <= len(L) + 1:
        if i not in L:
    		return i
        i = i + 1