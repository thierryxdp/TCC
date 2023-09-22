def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
	i=0
    lista=[1::len(L)]
    if L==lista:
        termo_faltante=len(L)+1
    if L[0]!=1:
        termo_faltante=1
    else:
    	while L[i]+1==i+2:
        	termo_faltante=i+2
        	i=i+1
    return termo_faltante