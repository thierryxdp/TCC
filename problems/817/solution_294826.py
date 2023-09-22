def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos, retorna uma lista ordenada
    com as notas ficaram acima da media
    lista -> lista'''
	
	media= sum(lista)/len(lista)

	list.sort(lista)
	indice = list.index(lista,media)
	
	
	return indice