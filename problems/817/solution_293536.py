def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
    if M in P:
		list.remove(P,M)
  		return P[t+1:]
    else:
        return P[t+1:]