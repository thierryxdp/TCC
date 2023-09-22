def maiores(lista,n):
	"""A função adiciona na lista o número n, coloca a lista 
	em ordem e retorna outra lista com números maiores que n;
	list,int -> list"""
    newlist = lista
    list.append(lista, n)
    list.sort(newlist)
    n_position = list.index(newlist, n)
    return newlist[n_position+1:]

def acima_da_media(lista,n):
    newlist = lista
    media = sum(newlist)/len(lista)
    return media+n-n