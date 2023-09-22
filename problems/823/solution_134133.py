def faltante(L):
    """
    	retorna o número correspondente a peça faltante
    	list -> int
    """
    L.sort()
    i=0
    while i<len(L):
        if L[i]==1+i:
            i+=1
        else:
            return L[i]