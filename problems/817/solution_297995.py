def acima_da_media(lista):
	media = sum(lista)/len(lista)
    int(media)
    lista.append(media)
    lista.sort()
    index = lista.index(media)
    lista.remove(media)
	return lista[index:]