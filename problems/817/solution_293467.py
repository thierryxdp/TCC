def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
	return list.remove(P[t+1:],M)