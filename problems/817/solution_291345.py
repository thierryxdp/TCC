def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista
def maiores(lista,n):
    for x in insere(lista,n)[:(list.index(lista,n)+1)]:
        list.remove(lista,x)
    return lista
def acima_da_media(lista):
    media=sum(lista)/len(lista)
    while media in lista:
    	list.remove(lista,media)
	return maiores(lista,media)