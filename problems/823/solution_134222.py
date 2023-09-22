def faltante(L):
    list.sort(L)
    L[0]=1
    L[-1]=n
    len(L)=n-1
    indice=0
    while indice<len(L):
        if L[indice+1]-L[indice]==1:
        	indice=indice+1
        elif L[indice+1]-L[indice]=2:
            return L[indice+1]+L[indice]/2