def acima_da_media(lista):
	"""Função que retorna uma lista ordenada com as notas dos alunos que ficaram acima da média
	lista -> lista"""
	
	media = sum(lista)/len(lista)
	lista_ordenada = lista + [media]
	lista_ordenada.sort()
	indice = lista_ordenada.index(media)
	
	return lista_ordenada[indice + 1:]