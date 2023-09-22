def acima_da_media(lista):
	'''Função que recebe uma lista com as notas dos alunos de uma turma e retorna uma
	lista ordenada com as notas que ficaram acima da média.
	Entrada: lista
	Saída: lista'''
	if list.index(lista,media)==True:
		list.sort(lista,reverse=True)
		media=sum(lista)//len(lista)
		localizacao=list.index(lista,media)
		lista=lista[0:localizacao]
		list.sort(lista)
		return lista
	else:
		list.sort(lista,reverse=True)
		media=sum(lista)//len(lista)
		lista=lista[0:media]
		list.sort(lista)
		return lista