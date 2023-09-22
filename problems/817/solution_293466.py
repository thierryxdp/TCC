def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
   	K=P[t+1:]
	return list.remove(K,M)