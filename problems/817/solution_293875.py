def acima_da_media(lista):
'''retorna as noas acima da media 
   dada uma lista com as mesmas
   list->list'''
	L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
    if M in P[t+1:]:
        list.remove(P,M)
	return P[t+1:]