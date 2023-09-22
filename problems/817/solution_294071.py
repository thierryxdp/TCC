def acima_da_media(lista_de_notad):
	media_notas = sum(lista_de_notas)/len(lista_de_notas)
	if media_notas not in lista_de_notas:
		list.append(lista_de_notas,media_notas)
	list.sort(lista_de_notas)
	indice = list.index(lista_de_notas, media_notas)
	return lista[indice+1:]