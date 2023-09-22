def faltante(L):
    """Esse funcao retorna o numero faltante de uma lista L;
    list -> int
    """
    
    n = len(L)
    i = 0
    
    while i < n:
        if i not in L:
            return i
        i = i + 1