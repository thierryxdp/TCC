def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
	i=0
	total_pecas=len(L)+1
    while i<total_pecas-1:
        if i+1 not in L:
            faltante=i+1
        if L[i] != i+1:
            faltante=i+1
    	else:
            i=i+1
return faltante