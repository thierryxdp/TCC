def acima_da_media(lista_nota):
    'função que retorna lista com as notas dos alunos com nota acima da média'
	'list,int--> list'
	lista = sum(lista_nota)
	media = lista/len(lista_nota)
	m = round (media,1)
	l = lista_nota[0:] + [m]
	list.sort(l)
	x = list.index(l, m)
	nova_lista = l[(x+1)::]
	return nova_lista