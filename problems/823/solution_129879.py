def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
	i=0
	total_pecas=len(L)+1
    faltante=""
    while i<pecas:
        if i+1 not in lista:
            faltante=i+1
        if L[i] != i+1:
            faltante=i+1
    i=i+1
    return faltante