def acima_da_media (nota):
	'''funcao querecebe lista com as notas dos alunos e retorna notas acima da media.
		int->int'''
	soma = sum(nota)
	qTotal = len(nota)
	media = (soma//qTotal)
	list.append(nota,media)
	list.sort(nota)
	list.reverse(nota)
	total = list.index(nota,media)
	lista = nota[0:total]
	list.sort(lista)
	return lista