def acima_da_media(lista):
	media_notas = sum(lista)/len(lista)
	if media_notas not in lista:
		list.append(lista,media_notas)
	list.sort(lista)
	indice = list.index(lista, media_notas)
	return lista[indice+1:]