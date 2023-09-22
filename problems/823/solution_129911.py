def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
	i=0
	total_pecas=len(L)+1
    while i<total_pecas-2:
        if i+1 not in L:
            return faltante=i+1
    	else:
            i=i+1