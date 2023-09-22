def faltante(L):
    """
    	retorna o número correspondente à peça que está faltando
    	list -> int
    """
    L.sort()
    if L[0]!=1:
        return 1
    L.reverse()
    i=0
    while i<=len(L):
        if L[i]==len(L)+1-i:
            i+=1
        else:
            return L[i]+1