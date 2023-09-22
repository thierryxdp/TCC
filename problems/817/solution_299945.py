def acima_da_media(lista_nota):
    'função que retorna lista com as notas dos alunos com nota acima da média'
	'list,int--> list'
	lista = sum(lista_nota)
	media = lista/len(lista_nota)
	l = lista_nota[0:] + [media]
	list.sort(l)
	x = list.index(l, media)
	nova_lista = lista_nota[(x+1):]
	return nova_lista