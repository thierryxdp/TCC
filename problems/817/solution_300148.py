def maiores(lista, n):   
    list.append(lista,n)
	list.sort(lista)
    return lista[list.index(lista,n)+1:]
def acima_da_media(lista):
    '''asdasa'''
    media = sum(lista)/(len(lista))
    return maiores(lista, ceil(media))