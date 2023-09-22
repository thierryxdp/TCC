def acima_da_media(lista_nota):
    'função que retorna lista com as notas dos alunos com nota acima da média'
	'list,int--> list'
	lista = sum(lista_nota)
	media = lista/len(lista_nota)
	m = round (media,1)
	l = lista_nota
	list.sort(l)
	notas_acima_media = [l for l in l if l > m]
	return notas_acima_media