def faltante(L):
    """Retorna o numeoro faltante na lista dada como entrada
    list -> int"""
    
    n = len(L)
    i = 1
    
    while i <= n+1:
        if i not in L:
    		return i
        i = i + 1