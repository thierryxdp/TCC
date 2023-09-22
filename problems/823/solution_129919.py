def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
	i=0
	total_pecas=len(L)+1
	while i<len(L):
        if i+1 not in L:
            faltante=i+1
            return faltante
        if L[-1]==len(L):
            faltante=len(L)+1
            return faltante
        else:
            i=i+1