def acima_da_media(lista):
    def maiores(lista, n):
    	list.append(lista,n)
    	list.sort(lista)
    	return lista[list.index(lista,n)+1:]
    media = sum(lista)/len(lista)
    if(media in lista):
        nova = maiores(lista,media)
        return nova[1:]
    else:
    	return maiores(lista,media)