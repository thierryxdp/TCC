def maiores(lista,n):
	'''retorna uma sublista dada uma lista os elementos 
    maiores que n
    list,int->list'''   
    L=lista
    L=lista+[n]
    list.sort(L)
    t=list.index(L,n)
    return L[t+1:]