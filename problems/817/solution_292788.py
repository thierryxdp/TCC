def acima_da_media(lista):
    media = sum(lista)/len(lista)
	if not media in lista:
    	list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
    lista1 = lista[posicao+1 :]
    return lista1