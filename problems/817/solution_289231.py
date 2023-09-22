def acima_da_media(lista):
	'''Função que recebe uma lista com as notas dos alunos de uma turma e retorna uma
	lista ordenada com as notas que ficaram acima da média.
	Entrada: lista
	Saída: lista'''
	media=sum(lista)//len(lista)
	if media in lista:
		list.sort(lista,reverse=True)
		localizacao=list.index(lista,media)
		lista=lista[0:localizacao]
		list.sort(lista)
		return lista
	else:
		lista.append(media)
		list.sort(lista,reverse=True)
		localizacao=list.index(lista,media)
		lista=lista[0:localizacao]
		list.sort(lista)
		return lista