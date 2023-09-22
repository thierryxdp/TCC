def acima_da_media2(lista):
	'''Função que recebe uma lista com as notas dos alunos de uma turma e retorna uma
	lista ordenada com as notas que ficaram acima da média.
	Entrada: lista
	Saída: lista'''
	list.sort(lista,reverse=True)
	media=sum(lista)//len(lista)
	localizacao=list.index(lista,media)
	lista=lista[0:localizacao]
	list.sort(lista)
	return lista