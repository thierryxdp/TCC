def acima_da_media(notas):
    """função que dada uma lista com notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média"""
    if len(notas)<=1:
    	return []
    else:
       	media=sum(notas)/len(notas)
       	lista=notas+[media]
       	list.sort(lista)
       	indice=lista.index(media)
      	 return lista[indice+1:]