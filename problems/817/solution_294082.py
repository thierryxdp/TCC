def acima_da_media(lista_de_notas):
    '''Função que dada uma lista de notas, retorna uma lista ordenada com as notas acima da média'''
    ''' list -> list '''
	media_notas = sum(lista_de_notas)/len(lista_de_notas)
	if media_notas not in lista_de_notas:
		list.append(lista_de_notas,media_notas)
	list.sort(lista_de_notas)
	indice = list.index(lista_de_notas, media_notas)
	return lista_de_notas[indice+1:]