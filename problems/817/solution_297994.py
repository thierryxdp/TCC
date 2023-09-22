def acima_da_media(lista):
	int(media) = sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    index = lista.index(media)
    lista.remove(media)
	return lista[index:]