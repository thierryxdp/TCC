def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
    i=0
    cont=0
    ultimo=L[-1]
    tamanho=len(L)
    if L[0]!=1:
        L[0:0]=[1]
        return L[0]
	elif L[-1]!=tamanho+1:
        list.append(L,tamanho+1)
    	return L[-1]
    else:
        while i<len(L):
            if L[i]==L[i-1]+2:
                L[i:i]=[i+1]
        		cont=cont+1
        	i=i+1
    	return cont