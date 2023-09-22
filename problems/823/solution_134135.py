def faltante(L):
    """
    	retorna o número correspondente a peça faltante
    	list -> int
    """
    L.sort()
    L.reverse()
    i=0
    while i<=len(L):
        if L[i]==len(L)+1-i:
            i+=1
        else:
            return L[i]+1