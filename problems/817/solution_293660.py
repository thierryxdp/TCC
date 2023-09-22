def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
   	Lf=P[t+1:]
    if M not in Lf:
		return P[t+1:]
    else:
        s=list.remove(Lf,M)
        return s